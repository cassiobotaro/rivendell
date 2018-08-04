import sys

import cv2

ENTER = 13

capture = cv2.VideoCapture('Lupi.AVI')
if capture is None:
    print("Video not found.", file=sys.stderr)
    sys.exit(1)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
output_size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
               int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = capture.get(cv2.CAP_PROP_FPS)
output = cv2.VideoWriter('videorgb2gray.avi', fourcc, fps, output_size,
                         isColor=0)

captured, frame = capture.read()
key = 0

while captured and key != ENTER:
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    output.write(gray_frame)
    cv2.imshow('video', frame)
    cv2.imshow('Black & white', gray_frame)
    captured, frame = capture.read()
    key = cv2.waitKey(delay=33)

capture.release()
output.release()
cv2.destroyAllWindows()
