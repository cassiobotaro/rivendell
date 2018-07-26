# Module to modify an image pixels based on it's position
import cv2
image = cv2.imread('lena.jpg')
height, width, _ = image.shape
for y in range(height):
    for x in range(width):
        image[y, x] = (x % 256, y % 256, x % 256)
cv2.imshow("Modified image", image)
cv2.waitKey(0)  # wait to press any key
