import sys

import cv2


def do_pyr_down(image):
    height, width, *_ = image.shape
    assert width % 2 == 0 and height % 2 == 0
    return cv2.pyrDown(image)


def do_canny(image, low_threshold, high_threshold, aperture):
    if len(image.shape) < 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(image, low_threshold, high_threshold,
                     apertureSize=aperture)


image = cv2.imread("lena.jpg")
if image is None:
    print("Image not found.", file=sys.stderr)
    sys.exit(1)
reduced_image = do_pyr_down(image)
canny = do_canny(image, low_threshold=10, high_threshold=100, aperture=3)
cv2.imshow("image", image)
cv2.imshow("reduced image", reduced_image)
cv2.imshow("canny", canny)
cv2.waitKey()
