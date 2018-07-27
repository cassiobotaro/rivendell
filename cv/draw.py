# Module to draw circles, rectangles and lines
import cv2

image = cv2.imread('lena.jpg')

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
cv2.line(image, (0, 0), (100, 200), GREEN)
cv2.line(image, (300, 200), (150, 150), RED, 5)
cv2.rectangle(image, (20, 20), (120, 120), BLUE, 10)
cv2.rectangle(image, (200, 50), (225, 125), GREEN, -1)
height, width, _ = image.shape
# image center
(X, Y) = (width // 2, height // 2)
for radius in range(0, 175, 15):
    cv2.circle(image, (X, Y), radius, RED)
cv2.imshow('Drawing over image', image)
cv2.waitKey(0)
