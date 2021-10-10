import numpy as np
import cv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',',y);
        font = cv2.FONT_HERSHEY_SIMPLEX;
        strXY = str(x) + ',' + str(y);
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 1);
        cv2.imshow('image', img);
     
    if event == cv2.EVENT_RBUTTONDOWN: 
        blue =img[y,x,0];
        green = img[y,x,1];
        red = img[y,x,2];
        strBGR = str(blue) + ',' + str(green) + ',' + str(red);
        font = cv2.FONT_HERSHEY_SIMPLEX;
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,255), 1);
        cv2.imshow('image', img)
 
img =  cv2.imread('Test.jpg') 
cv2.imshow('image',img);
cv2.resizeWindow('image',840, 640);
 
cv2.setMouseCallback('image',click_event);
 
cv2.waitKey(0);      