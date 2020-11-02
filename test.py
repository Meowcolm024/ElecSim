import cv2
import numpy

img = cv2.imread('assets/testc.png', cv2.IMREAD_GRAYSCALE)   

# print(img[53][35]//255)

cv2.imshow('show', img)
cv2.waitKey(0)    
cv2.destroyAllWindows()  

