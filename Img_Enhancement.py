#Image enhancement using CLAHE
#CLAHE stands for Contrast Limited Adaptive Histogram Equilization 

import cv2
#Read the image
img=cv2.imread('C:\\Users\\Isra\\Documents\\Coding\\Python\\crime.png')

#Preparation for CLAHE
clahe=cv2.createCLAHE()
 
#Convert to gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply enhancement
enh_img=clahe.apply(gray_img)

cv2.imwrite('C:\\Users\\Isra\\Documents\\Coding\\Python\\enhanced.png',enh_img)
print("Done Enhancement")