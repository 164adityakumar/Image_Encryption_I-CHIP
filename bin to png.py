import numpy as np
import cv2
f=open("D:/Aditya/Verilog/I CHIP/Enigma.txt","r")
a1=0
a2=0
b=0
c=128
z1=0
arr=np.zeros((1024,1024))
lines=f.readline()
print(lines)

#for y in f:
while(lines):
    lines = f.readline()
    for x in lines:
        b=b+c*int(x)
        c=c//2
    if(c==0):
            c=128
            arr[a1][a2]=b
            b=0
            print(a1)
            z1=z1+1
            if(a2==1023):
                if(a1==1023):
                    a1=123456
                a1=a1+1
                a2=0
            else:
                a2=a2+1
            if(z1==8):
                z1=0
                break
    if(a1==123457):
        break
image=cv2.imshow("image",arr.astype('uint8'))
#cv2.imwrite("D:/Aditya/Verilog/I CHIP/ecb_enc.bmp",image)
cv2.waitKey(0)
cv2.destroyAllWindows()