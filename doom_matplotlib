import numpy as np
import matplotlib.pyplot as plt

WIDTH, HEIGHT = 100, 100
PIXEL_SIZE = 1
W = WIDTH // PIXEL_SIZE
H = HEIGHT // PIXEL_SIZE

arr = np.zeros((H, W), dtype=np.uint8)
arr[-1]= 36
rng = np.random.default_rng()
cols = np.arange(0, W)
img = plt.imshow(arr, cmap=plt.cm.inferno, interpolation='nearest')
plt.draw()
plt.pause(0.01)
plt.draw()

for _ in range(1000):
    decay = rng.integers(0, 2, arr[1:].shape)
    shift = rng.choice([-1, 0, 1], arr[1:].shape, p=[0.1, 0.8, 0.1])
    arr[:-1] = np.take_along_axis(arr[:-1], (cols + shift) % W, axis=1)
    arr[:-1] = (arr[1:] - decay).clip(0)
    img.set_data(arr)
    plt.pause(0.001)
