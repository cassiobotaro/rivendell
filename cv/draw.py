# Module to draw circles, rectangles and lines
import cv2

image = cv2.imread('lena.jpg')

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
cv2.line(image, pt1=(0, 0), pt2=(100, 200), color=GREEN)
cv2.line(image, pt1=(300, 200), pt2=(150, 150), color=RED, thickness=5)
cv2.rectangle(image, pt1=(20, 20), pt2=(120, 120), color=BLUE, thickness=10)
cv2.rectangle(image, pt1=(200, 50), pt2=(225, 125), color=GREEN, thickness=-1)
height, width, _ = image.shape
# image center
center = (width // 2, height // 2)
for radius in range(0, 175, 15):
    cv2.circle(image, center, radius, RED)
cv2.imshow('Drawing over image', image)
cv2.waitKey(0)
