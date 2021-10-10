from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE);
_, mask = cv2.threshold(img, 220,255,cv2.THRESH_BINARY_INV);

kernel = np.ones((2,2),np.uint8);
dilation = cv2.dilate(mask,kernel,iterations=2); 
erosion = cv2.erode(mask,kernel,iterations=1);
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel);
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel);
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel);
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel);

titles = ['Original', 'Binary_INV','Dilation','Erosion','Opening','Closing','Gradient','Top Hat'];
images = [img,mask,dilation,erosion,opening,closing,mg,top_hat];


for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i],'gray');
    plt.title(titles[i]);
    plt.xticks([]),plt.yticks([]); 
    

plt.show();    
