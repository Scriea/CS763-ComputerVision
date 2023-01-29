import numpy as np
import cv2
import pickle
import argparse
import os
from os import listdir


img_path = "/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/data/captured/kids.jpg"
img = cv2.imread(img_path)
img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# folder_dir = "01/01/data/captured"
# for images in os.listdir(folder_dir):
 
    
#     # check if the image ends with png
#     if (images.endswith(".png")):
#         print(images)


print('Hello World')

# img_ini = img.copy()
# drawing = False
# ix,iy = -1,-1
# cood = []
# def draw_rectangle(event, x, y, flags, param):
#    global ix, iy, drawing, img
#    if event == cv2.EVENT_LBUTTONDOWN:
#       drawing = True
#       ix = x
#       iy = y
#    elif event == cv2.EVENT_LBUTTONUP:
#       drawing = False
#       cv2.rectangle(img, (ix, iy),(x, y),(0, 0, 0),0)
#       cood.append(((ix,iy),(x,y)))
    
# cv2.namedWindow("Rectangle Window")
    
# cv2.setMouseCallback("Rectangle Window", draw_rectangle)

# while True:
#    cv2.imshow("Rectangle Window", img)
#    if cv2.waitKey(1) == ord('q'):
#        break
#    if cv2.waitKey(1) == ord('r'):
#         img = img_ini
        
# cv2.destroyAllWindows()

# print(cood)