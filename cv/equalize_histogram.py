# Module to equalize image histogram
from matplotlib import pyplot as plt
import cv2

gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
equalized_histogram = cv2.equalizeHist(gray)

plt.figure()
plt.title('Equalized histogram')
plt.xlabel('Intensity')
plt.ylabel('Quantity of Pixels')
histogram_equalized = cv2.calcHist([equalized_histogram], channels=[0], mask=None,
                                   histSize=[256], ranges=[0, 256])
plt.plot(histogram_equalized)
plt.xlim([0, 256])
plt.savefig('equalized_histogram.png')
cv2.imwrite('equalized_histogram.jpg', equalized_histogram)

plt.figure()
plt.title('Original histogram')
plt.xlabel('Intensity')
plt.ylabel('Quantity of Pixels')
histogram_original = cv2.calcHist([gray], channels=[0], mask=None,
                                  histSize=[256], ranges=[0, 256])
plt.plot(histogram_original)
plt.xlim([0, 256])
plt.savefig('original_histogram.png')
cv2.imwrite('original_histogram.jpg', gray)

cv2.waitKey()
