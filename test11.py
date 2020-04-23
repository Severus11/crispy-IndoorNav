import cv2
from PIL import Image
import numpy as np
#image = cv2.imread("144-1448310_clip-art-homer-simpson-black-and-white-bart.png")
image= Image.open('144-1448310_clip-art-homer-simpson-black-and-white-bart.png')
im = np.array(image).resize(200,200)
print(im)