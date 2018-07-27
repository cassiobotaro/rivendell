# Module to crop an image
import cv2
image = cv2.imread("lena.jpg")
cropping = image[100:200, 100:200]
cv2.imshow("Image cropping", cropping)
cv2.waitKey(0)  # wait to press any key
cv2.imwrite("cropping.jpg", cropping)
