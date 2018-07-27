# Module to modify an image(yellow) pixels based on it's position
# jumping some pixels
import cv2
image = cv2.imread('lena.jpg')
height, width, _ = image.shape
YELLOW = (0, 255, 255)
for y in range(0, height, 10):  # iterate lines
    for x in range(0, width, 10):  # iterate columns
        image[y:y+5, x:x+5] = YELLOW
cv2.imshow('Modified image', image)
cv2.waitKey(0)  # wait to press any key
