import face_recognition as fr
import numpy as np
import cv2
import argparse
import os
import sys

def conv(i):
    a = str(i)
    if len(a) <2:
        return "0" + a
    return a

## Create Parser
parser = argparse.ArgumentParser(prog='face-makeup',
                                 description='Applies makeup to faces present in the image')
parser.add_argument('-i', "--data", help=' path of image data')
parser.add_argument('-o', "--faces", help='path for storing output')
parser.add_argument('-t', '--type', type = int, help='Takes path of the image for saving')


args = parser.parse_args()

data_dir = os.path.abspath(args.data)
saving_dir = os.path.abspath(args.faces)
filename = data_dir.replace('\\','/').split('/')[-1].split('.')[0]

if not os.path.isdir(data_dir):
    print("No such directory exist (try using raw path?)!")
    exit()

image = fr.load_image_file(data_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
face_locations = fr.face_locations(image)

for location in face_locations:
    top, right, bottom, left = location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

if args.type ==1:
    if len(face_locations) == 0:
        print("No face detected")
    else:
        for i,location in enumerate(face_locations):
            top, right, bottom, left  = location
            face = image[top:bottom, left:right]
            
            cv2.imshow("Image", face)
            if(len(face_locations) != 1):
                cv2.imwrite(saving_dir + "face" + filename + "suffix" + conv(i+1) + ".jpg", face)
            else:
                cv2.imwrite(saving_dir + "face" + filename + ".jpg", face)

        cv2.waitKey(0)        
        cv2.destroyAllWindows()

if args.type ==2:
    ## Video
    pass
