import sys
import cv2

image = cv2.imread("lena.jpg")
if image is None:
    print("Image not found.", file=sys.stderr)
    sys.exit(1)
smooth = cv2.GaussianBlur(image, ksize=(0, 0), sigmaX=4)
cv2.imshow("image", image)
cv2.imshow("smooth", smooth)
cv2.waitKey()
