# Module that apply a bitwise and mask
import cv2
import numpy as np
image = cv2.imread('lena.jpg')
cv2.imshow('Original', image)
height, width, _ = image.shape
mask = np.zeros((height, width), dtype=np.uint8)
center = (width // 2, height // 2)
cv2.circle(mask, center, radius=100, color=255, thickness=-1)
masked_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Mask applied to image', masked_image)
cv2.waitKey(0)
