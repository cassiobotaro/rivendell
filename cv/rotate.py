# Module to rotate an image
import cv2
image = cv2.imread('lena.jpg')
height, width, _ = image.shape  # caught height and width
center = (width // 2, height // 2)  # find the center
rotation_matrix = cv2.getRotationMatrix2D(center, 30, 1.0)  # 30 degrees
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow("Image rotated 30 degrees", rotated_image)
cv2.waitKey(0)
