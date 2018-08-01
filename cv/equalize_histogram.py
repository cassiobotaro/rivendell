# Module to equalize image histogram
from matplotlib import pyplot as plt
import cv2

gray = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
equalized_histogram = cv2.equalizeHist(gray)

plt.figure()
plt.title('Equalized histogram')
plt.xlabel('Intensity')
plt.ylabel('Quantity of Pixels')
plt.hist(equalized_histogram.ravel(), bins=256, range=[0, 256])
plt.xlim([0, 256])
plt.savefig('equalized_histogram.png')
cv2.imwrite('equalized_histogram.jpg', equalized_histogram)

plt.figure()
plt.title('Original histogram')
plt.xlabel('Intensity')
plt.ylabel('Quantity of Pixels')
plt.hist(gray.ravel(), bins=256, range=[0, 256])
plt.xlim([0, 256])
plt.savefig('original_histogram.png')
cv2.imwrite('original_histogram.jpg', gray)

cv2.waitKey()
