import numpy as np
import cv2

img=cv2.imread('C:/Users/hp/Downloads/Input Image.jpg',0)
w,h=1024,1024
z=0
c=0
f=open("binary.txt","a")
print("opened file")
for i in range(w):
    for j in range(h):
        a=img[i][j]
        l = []
        for k in range(8):
            b=a%2
            l.append(b)
            a=a//2
        for ele in reversed(l):
            f.write(str(ele))
            c=c+1
        z=z+1
        if(z==8):
            f.write('\n')
            z=0
            print("complete")
