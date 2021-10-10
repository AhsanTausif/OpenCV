import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB);

kernel = np.ones((5,5), np.float32)
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gaussian_blur = cv2.GaussianBlur(img, (5,5), 0)  ### Gaussian Blur removes high frequency noise from images

median = cv2.medianBlur(img, 5)   ### sorts out salt and pepper noise
bilateral = cv2.bilateralFilter(img, 9, 75, 75)   ### helps removing noise while keeping edges sharp

titles = ['image','2D Convulation', 'Blur', 'GaussianBlur','median','bilateral']
images = [img,dst,blur,gaussian_blur,median,bilateral]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    

plt.show()    