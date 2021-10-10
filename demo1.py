import cv2

img = cv2.imread('Test.jpg',1);
print(img);

cv2.imshow('image', img);
cv2.resizeWindow('image',840, 640);
k = cv2.waitKey(0);

if(k==27):
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('Test2.png', img);
    cv2.destroyAllWindows();