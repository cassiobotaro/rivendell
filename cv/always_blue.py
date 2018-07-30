# Module to modify an image pixels to blue
import cv2
image = cv2.imread('lena.jpg')
height, width, _ = image.shape
BLUE = (255, 0, 0)
for y in range(height):
    for x in range(width):
        image[y, x] = BLUE
cv2.imshow('Modified image', image)
cv2.waitKey(0)  # wait to press any key
