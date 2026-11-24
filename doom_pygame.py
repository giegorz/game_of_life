import sys
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt

WIDTH, HEIGHT = 1000, 1000
PIXEL_SIZE = 10
W = WIDTH // PIXEL_SIZE
H = HEIGHT // PIXEL_SIZE
MAX_VAL = 30

arr = np.zeros((H, W), dtype=np.uint8)
arr[-1]= MAX_VAL
rng = np.random.default_rng()
cols = np.arange(0, W)
colors = (plt.cm.afmhot(np.linspace(0, 1, MAX_VAL + 1))[:, :3] * 255).astype(np.uint8)

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    decay = rng.integers(0, 2, arr[1:].shape)
    shift = rng.choice([-1, 0, 1], arr[1:].shape, p=[0.1, 0.8, 0.1])
    arr[:-1] = np.take_along_axis(arr[:-1], (cols + shift) % W, axis=1)
    arr[:-1] = (arr[1:] - decay).clip(0)
    rgb = colors[arr]
    surface = pg.surfarray.make_surface(rgb.swapaxes(0, 1))
    scaled = pg.transform.scale(surface, (WIDTH, HEIGHT))
    screen.fill((0, 0, 0))
    screen.blit(scaled, (0, 0))
    pg.display.flip()
    clock.tick(45)
