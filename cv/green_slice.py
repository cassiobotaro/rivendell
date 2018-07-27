# Module to change a slice of pixels into green
import cv2
image = cv2.imread('lena.jpg')
# from 30 to 50 in y color pixel to green
image[30:50, :] = (0, 255, 0)
cv2.imshow("Modified image", image)
cv2.waitKey(0)  # wait to press any key
