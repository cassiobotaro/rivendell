# Module to flip an image
import cv2
image = cv2.imread('lena.jpg')
cv2.imshow('Original', image)
horizontal_flip = image[::-1, :]  # command below
# horizontal_flip = cv2.flip(image, 1)
cv2.imshow('Horizontal Flip', horizontal_flip)
vertical_flip = image[:, ::-1]  # command below
# vertical_flip = cv2.flip(img, 0)
cv2.imshow('Vertical Flip', vertical_flip)
hv_flip = image[::-1, ::-1]  # command below
# hv_flip = cv2.flip(img, -1)
cv2.imshow('Horizontal and Vertical Flip', hv_flip)
cv2.waitKey(0)
