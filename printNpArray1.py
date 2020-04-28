import cv2
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

img = cv2.imread("/home/severus7/Documents/python/test.png")

r1 = np.array([0,0,0])
r2 = np.array([10,10,10])
    
#img= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#mask = cv2.inRange(img,r1,r2)

ret,img = cv2.threshold(img,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
img = cv2.erode(img, kernel, iterations=3)

dilated_Edges = cv2.dilate(img, kernel, iterations=2)

elements=[]
for i in range(0,1000):
    elements.append([])

def main():
    for i in range(0,1000):
        
        for  j in range(0,800):
            c = img[i,j]
            #c= pixel[0]+pixel[1]+pixel[2]
            if (c<2):
                val = 1
                elements[i].append(val)
            else:
                val=0
                elements[i].append(val)
    
    grid= np.array(elements)

    start = (0,0)
    goal= (9,15)
    fig, ax= plt.subplots(figsize=(12,12))
    ax.imshow(grid, aspect ='auto', cmap=plt.get_cmap('binary'))
    #ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
    #ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
    plt.show()

    #cv2.imshow('test', img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows

if __name__ == "__main__":
    main()

    



