# Module to read one pixel
import cv2

image = cv2.imread('lena.jpg')
b, g, r = image[0, 0]
print('The pixel (0, 0) has the following colors:')
print(f'Red: {r}, Green: {g}, Blue: {b}')
