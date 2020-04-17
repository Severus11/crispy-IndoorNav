import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
while(1):
    ret,frame= cap.read()
    
    r1 = np.array([90, 100 , 100])
    r2 = np.array([150,255,255])
    
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    grayscaled= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    mask = cv2.inRange(hsv,r1,r2)

    ret,bw = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
    bw = cv2.erode(bw, kernel, iterations=3)

    dilated_Edges = cv2.dilate(bw, kernel, iterations=2)
    
    cv2.imshow("bw", bw)
    #cv2.imshow('frame',mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows