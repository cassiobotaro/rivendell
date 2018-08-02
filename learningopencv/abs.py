import cv2

image1 = cv2.imread("cruzeiro_tux_2010_normal.png")
image2 = cv2.imread("th_2013.png")
absdiff = cv2.absdiff(image1, image2)
absdiffs = cv2.absdiff(absdiff, (100, 0, 0, 0))
cv2.imshow("absdiff", absdiff)
cv2.imshow("absdiffs", absdiffs)
cv2.waitKey()
