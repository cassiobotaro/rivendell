import sys

import cv2

image = cv2.imread("lena.jpg")
if image is None:
    print("Image not found.", file=sys.stderr)
    sys.exit(1)
cv2.imshow("image", image)
cv2.waitKey()
