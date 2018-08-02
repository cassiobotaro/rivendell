import cv2

image1 = cv2.imread("cruzeiro_tux_2010_normal.png")
image2 = cv2.imread("th_2013.png")
add = cv2.add(image1, image2)
adds = cv2.add(image1, (0, 10, 30, 100))
cv2.imshow("add", add)
cv2.imshow("adds", adds)
cv2.waitKey()
