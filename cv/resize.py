# Module to resize an image
import cv2
image = cv2.imread('lena.jpg')
cv2.imshow('Original', image)
height, width, _ = image.shape
proportion = 100.0 / width
new_size = (100, int(height * proportion))
resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
cv2.imshow('Resized image', resized_image)
cv2.waitKey(0)
