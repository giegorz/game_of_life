import sys

import numpy as np
import pygame as pg

SIZE = WIDTH, HEIGHT = 2560, 1440
PIXEL_SIZE = 10
H, W = HEIGHT // PIXEL_SIZE, WIDTH // PIXEL_SIZE
rng = np.random.default_rng()
arr = rng.choice([0,1], size=(H, W), p=[0.6, 0.4]).astype(np.uint8)

def step(arr: np.ndarray) -> np.ndarray:
    p = np.pad(arr, 1)
    s = (
          p[:-2, :-2]
        + p[:-2, 1:-1]
        + p[:-2, 2:]
        + p[1:-1, :-2]
            #center
        + p[1:-1, 2:]
        + p[2:, :-2]
        + p[2:, 1:-1]
        + p[2:, 2:]
    )

    alive = arr == 1
    survives = alive & np.isin(s, (2,3))
    born = ~alive & (s == 3)

    return (survives | born).astype(np.uint8)

pg.init()
pg.display.set_caption("Gol")
screen = pg.display.set_mode(SIZE)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    arr = step(arr)

    screen.fill((0, 0, 0))
    surface = pg.surfarray.make_surface(arr.swapaxes(0, 1) *255)
    scaled = pg.transform.scale(surface, SIZE)
    screen.blit(scaled, (0, 0))
    
    pg.display.flip()
    clock.tick(30)
