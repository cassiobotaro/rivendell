# Module to modify an image pixels based on it's position
# Just modify green component
import cv2
image = cv2.imread('lena.jpg')
height, width, _ = image.shape
for y in range(height):
    for x in range(width):
        image[y, x] = (0, (x * y) % 256, 0)
cv2.imshow('Modified image', image)
cv2.waitKey(0)  # wait to press any key
