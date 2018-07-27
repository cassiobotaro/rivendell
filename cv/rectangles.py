# Module to draw rectangles in the image
import cv2
image = cv2.imread('lena.jpg')
# Creates a blue rectangle over the entire width of the image
image[30:50, :] = (255, 0, 0)
# Creates a red square
image[100:150, 50:100] = (0, 0, 255)
# Created a yellow rectangle all over the image height
image[:, 200:220] = (0, 255, 255)
# Creates a green rectangle from line 150 to 300 on columns 250 to 350
image[150:301, 250:351] = (0, 255, 0)
# Creates a cyan square from line 300 to 400 on columns 50 to 150
image[300:401, 50:251] = (255, 255, 0)
# Creates a white square
image[250:350, 300:400] = (255, 255, 255)
# Creates a black rectangle
image[70:100, 300: 450] = (0, 0, 0)

cv2.imshow('Altered image', image)
cv2.imwrite('rectangles.jpg', image)
cv2.waitKey(0)
