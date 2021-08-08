import os 
import cv2 as cv 
import numpy as np

people=['SALMAN','SRK','CHRIS']
DIR=r'C:\Users\VISHWAS\Desktop\Opencv\Photos'
features=[]
label=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)

        for ig in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            face_rect=haar_cascade