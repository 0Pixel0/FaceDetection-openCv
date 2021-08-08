import cv2 as cv
import numpy as np
img=cv.imread('Photos/people.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
cv.imshow('people',img)
haar_casc=cv.CascadeClassifier('haar.xml')
face_rect=haar_casc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2)
print(f'no. of face detected={len(face_rect)}')
#now to draw rectangle on detected face
for(a,b,c,d) in face_rect:
    cv.rectangle(img,(a,b),(a+c,b+d),(0,255,0),thickness=2)
    cv.imshow("detected",img)



cv.waitKey(0)