# Module that split color channels
import cv2
image = cv2.imread('lena.jpg')
blue_channel, green_channel, red_channel = cv2.split(image)
cv2.imshow('Original', image)
cv2.imshow('Red', red_channel)
cv2.imshow('Green', green_channel)
cv2.imshow('Blue', blue_channel)
cv2.waitKey(0)
