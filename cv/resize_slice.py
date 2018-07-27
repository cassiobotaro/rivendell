# Module to resize an image using slicing
import cv2
image = cv2.imread("lena.jpg")
cv2.imshow("Original", image)
resized_image = image[::2, ::2]
cv2.imshow("Resized image", resized_image)
cv2.waitKey(0)
