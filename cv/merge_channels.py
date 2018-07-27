# Module that split color channels and merge with empty channels to generate
# specific colored images
import cv2
import numpy as np

image = cv2.imread("lena.jpg")
blue_channel, green_channel, red_channel = cv2.split(image)
zeros = np.zeros(image.shape[:2], dtype=np.uint8)

cv2.imshow('Red', cv2.merge([zeros, zeros, red_channel]))
cv2.imshow('Green', cv2.merge([zeros, green_channel, zeros]))
cv2.imshow('Blue', cv2.merge([blue_channel, zeros, zeros]))
cv2.imshow('Original', image)
cv2.waitKey(0)
