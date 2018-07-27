# Module to write a text into an image
import cv2
image = cv2.imread('lena.jpg')
font = cv2.FONT_HERSHEY_TRIPLEX
# cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[,
# lineType[, bottomLeftOrigin]]]) → None
cv2.putText(image, 'Lena', (15, 65), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("Lena", image)
cv2.waitKey(0)
