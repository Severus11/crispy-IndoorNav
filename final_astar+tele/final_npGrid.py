import cv2
import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#try making it all one function



def imgop(image):
    image = cv2.imread(image)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, img= cv2.threshold(img,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 3))
    img = cv2.erode(img, kernel, iterations=3)
    dilated_Edges = cv2.dilate(img, kernel, iterations=2)

    width= 800
    height = 800
    dim=(width, height)

    img= cv2.resize(img,dim , interpolation= cv2.INTER_AREA)

    start = (420,350)
    goal= (98,86)

    #print(grid)
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



def heuristic(a,b):
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def a_search(array,start, goal):
    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    close_set = set()
    previous_block = {}
    g = {start:0}
    f = {start:heuristic(start, goal)}
    
    oheap=[]
    heapq.heappush(oheap, (f[start], start))
    while oheap:
        current = heapq.heappop(oheap)[1]
        if current == goal:
            list1=[]
            while current in previous_block:
                list1.append(current)
                current= previous_block[current]
            return list1
        else:
            close_set.add(current)
            for i,j in neighbors:
                neighbor= current[0]+i, current[1]+j
                gs= heuristic(current, neighbor) +g[current]
                if 0 <= neighbor[0] < array.shape[0]:
                    if 0 <= neighbor[1] < array.shape[1]:                
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue
                if neighbor in close_set and gs >= g.get(neighbor, 0):
                    continue
                if gs<g.get(neighbor,0) or neighbor not in [i[1] for i in oheap]:
                    previous_block[neighbor]= current
                    g[neighbor]= gs
                    f[neighbor]= gs + heuristic(neighbor, current)
                    heapq.heappush(oheap, (f[neighbor], neighbor))


def main():
    #img = cv2.imread("/home/severus7/Documents/python/test.png")
    
    route= a_search(grid, start, goal)
    print(route)

    xc=[]
    yc=[]

    for i in range(0,len(route)):
        xc.append(route[i][0])
        yc.append(route[i][1])

    fig, ax= plt.subplots(figsize=(800,800))
    ax.imshow(grid, aspect ='auto', cmap=plt.get_cmap('binary'))
    ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
    ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
    #plt.show()
    ax.plot(yc,xc, color = "black")
    plt.show()
    plt.savefig('hero.jpg')


if __name__== "__main__":
    main()
    
    
