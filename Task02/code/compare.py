import numpy as np
import argparse
import face_recognition as fr
import cv2
import os
import sys

parser = argparse.ArgumentParser(prog='face-makeup',
                                 description='Applies makeup to faces present in the image')
parser.add_argument('-i', "--data", help=' path of image data')
args = parser.parse_args()

data_dir = os.path.abspath(args.data)

if not os.path.isdir(data_dir):
    print("No such directory exist (try using raw path?)!")
    exit()

image = fr.load_image_file(data_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
face_locations = fr.face_locations(image)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')