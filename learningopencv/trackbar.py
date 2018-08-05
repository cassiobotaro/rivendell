import sys

import cv2

ENTER = 13


def on_trackbar_slide(position):
    capture.set(cv2.CAP_PROP_POS_FRAMES, position)


capture = cv2.VideoCapture('Lupi.AVI')
if capture is None:
    print("Video not found.", file=sys.stderr)
    sys.exit(1)
cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
if frames != 0:
    cv2.createTrackbar("Position", "Video", 0, frames, on_trackbar_slide)
captured, frame = capture.read()
key = 0

while captured and key != ENTER:
    cv2.imshow("Video", frame)
    captured, frame = capture.read()
    key = cv2.waitKey(delay=33)

capture.release()
cv2.destroyAllWindows()
