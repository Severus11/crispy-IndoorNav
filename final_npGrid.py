import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

img = cv2.imread("/home/severus7/Documents/python/test.png")


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img= cv2.threshold(img,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
img = cv2.erode(img, kernel, iterations=3)
dilated_Edges = cv2.dilate(img, kernel, iterations=2)

width= 800
height = 800
dim=(width, height)

img= cv2.resize(img,dim , interpolation= cv2.INTER_AREA)






def npGrid():
    elements=[]
    for i in range(0,800):
        elements.append([])
    
    for i in range(0,800):
        for j in range(0,800):
            c= img[i,j]
            if(c<5):
                val =1
                elements[i].append(val)
            else:
                val =0
                elements[i].append(val)
    
    grid = np.array(elements)

    start = (420,350)
    goal= (98,86)
    fig, ax= plt.subplots(figsize=(12,12))
    ax.imshow(grid, aspect ='auto', cmap=plt.get_cmap('binary'))
    ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
    ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
    plt.show()

def main():
    #img = cv2.imread("/home/severus7/Documents/python/test.png")
    npGrid()


if __name__== "__main__":
    main()
    
    
