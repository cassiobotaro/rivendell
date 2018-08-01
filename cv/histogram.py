# Module that plot gray scale image histogram
import cv2
import matplotlib.pyplot as plt

gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray Image', gray)
histogram = cv2.calcHist([gray], channels=[0], mask=None,
                         histSize=[256], ranges=[0, 256])
plt.figure()
plt.title('Histogram')
plt.xlabel('Intesity')
plt.ylabel('Quantity of Pixels')
plt.plot(histogram)
plt.xlim([0, 256])
# Another way to plot histogram
# plt.hist(gray.ravel(), bins=256, range=[0, 256])
plt.savefig('histogram.png')
cv2.waitKey()
