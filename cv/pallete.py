# module to generate images based on colors
import numpy as np
import cv2

width = height = 100
channels = 3

# name -> b,g,r
colors = {
    "white": (255, 255, 255),
    "red": (0, 0, 255),
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "cyan": (255, 255, 0),
    "magenta": (255, 0, 255),
    "yellow": (0, 255, 255),
    "black": (0, 0, 0),
}

for name, color in colors.items():
    image = np.ndarray(shape=(width, height, channels), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            image[y, x] = color
        cv2.imwrite(f"pallete/{name}.jpg", image)
