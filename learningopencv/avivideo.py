import sys

import cv2

ENTER = 13

capture = cv2.VideoCapture('Lupi.AVI')
if capture is None:
    print("Video not found.", file=sys.stderr)
    sys.exit(1)

captured, frame = capture.read()
key = 0

while captured and key != ENTER:
    cv2.imshow('video', frame)
    captured, frame = capture.read()
    key = cv2.waitKey(delay=33)

capture.release()
cv2.destroyAllWindows()
