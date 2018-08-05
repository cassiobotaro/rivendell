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
output = cv2.VideoWriter('logpolar.avi', fourcc, fps, output_size,
                         isColor=1)

captured, frame = capture.read()
key = 0

while captured and key != ENTER:
    width, height = output_size
    logpolar_frame = cv2.warpPolar(
        src=frame,
        dsize=output_size,
        center=(width//2, height//2),
        maxRadius=40,
        flags=cv2.INTER_LINEAR+cv2.WARP_FILL_OUTLIERS+cv2.WARP_INVERSE_MAP
    )
    output.write(logpolar_frame)
    cv2.imshow('video', frame)
    cv2.imshow('Logpolar', logpolar_frame)
    captured, frame = capture.read()
    key = cv2.waitKey(delay=33)

capture.release()
output.release()
cv2.destroyAllWindows()
