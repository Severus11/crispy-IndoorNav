import cv2
import numpy as np

img = cv2.imread("/home/severus7/Documents/python/astar/shalini-misra-chattarpur-new-delhi-400x400.jpg")

img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


elements=[]
for i in range(0,400):
    elements.append([])

def main():
    for i in range(0,400):
        
        for  j in range(0,400):
            pixel = img[i,j]
            #print(val)

            #000one(pixel)
            c= pixel[0]+pixel[1]+pixel[2]
            if (c<35):
                val = 1
                #print(val)
                #elements[0].append(val)
            else:
                val=0
                #print(val)
            elements[i].append(val)
    

    #cv2.imshow('img',img)

    #cv2.waitKey(0)
    #cv2.destroyAllWindows
                
            
            
            
    
    #print(elements)
    #print("*********************************************************")

    a= np.array(elements)

    print(a)




if __name__ == "__main__":
    main()



