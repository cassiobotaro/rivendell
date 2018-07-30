# Module to get image metadata
import cv2

image = cv2.imread('lena.jpg')
height, width, channels = image.shape
print(f'Width in pixels: {width}')
print(f'Height in pixels: {height}')
print(f'Qty of channels: {channels}')
# Show image using function imshow
cv2.imshow('Window\'s name', image)
cv2.waitKey(0)  # wait to press any key
# Save image into disk using function imwrite()
cv2.imwrite('output.jpg', image)
