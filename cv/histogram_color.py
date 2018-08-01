# Module that plot color image histogram
import cv2
import matplotlib.pyplot as plt

color = cv2.imread('lena.jpg')
cv2.imshow('Color Image', color)

# split channels
channels = cv2.split(color)
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Histogram')
plt.xlabel('Intesity')
plt.ylabel('Quantity of Pixels')

for channel, color in zip(channels, colors):
    # one loop for each channel
    hist = cv2.calcHist([channel], channels=[0], mask=None,
                        histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.savefig('histogram-color.png')
cv2.waitKey()
