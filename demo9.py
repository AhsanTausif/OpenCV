import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Sudoku.png',cv2.IMREAD_GRAYSCALE)
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=1)  ### 64 Bit Float which helps dealing with negative nums
lap = np.uint8(np.absolute(lap)) ### convert lap into unsigned 8-bit integer
sobel_x = cv2.Sobel(img,cv2.CV_64F,1,0) 
sobel_y = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobel_x))
sobelY = np.uint8(np.absolute(sobel_y))
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image','Laplacian','Sobel_X','Sobel_Y','sobelCombined']
images = [img,lap,sobelX,sobelY,sobelCombined]

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    

plt.show() 