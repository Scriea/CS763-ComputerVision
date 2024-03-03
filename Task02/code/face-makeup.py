import numpy as np
import argparse
import face_recognition as fr
import cv2
import os
import sys

## Create Parser
parser = argparse.ArgumentParser(prog='face-makeup',
                                 description='Applies makeup to faces present in the image',
                                 )
parser.add_argument('-i', help='Takes path of the image for the operation')
parser.add_argument('-o', help='Takes path of the image for saving')
parser.add_argument('-t', '--type', type = int, help='Takes path of the image for saving')


args = parser.parse_args()

##Directory

img_dir = args.i
saving_dir = args.o

print(os.path.abspath(img_dir), os.path.normpath(saving_dir))

##Loading

image = fr.load_image_file(img_dir)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
original = image.copy()
landmarks = fr.face_landmarks(image)

## Draw contours
if(args.type == 1):
	for face in landmarks:
		for landmark in face:
			contour = np.asarray(face[landmark]).reshape(-1,1,2)
			image = cv2.polylines(image,[contour], False, (255,255,255))


## Makeup
if(args.type == 2):
	for face in landmarks:
		## Eyebrow

		contour = np.asarray(face['left_eyebrow']).reshape(-1,1,2)
		image = cv2.fillPoly(image,[contour], (39,54,68))
		image = cv2.addWeighted(image, 0.6, original, 0.4,0)
		image = cv2.polylines(image,[contour], False, (59,59,78),2)

		original = image.copy()

		contour = np.asarray(face['right_eyebrow']).reshape(-1,1,2)
		image = cv2.fillPoly(image,[contour], (39,54,68))
		image = cv2.addWeighted(image, 0.6, original, 0.4,0)
		image = cv2.polylines(image,[contour], False, (59,59,78),2)
		
		original = image.copy()

		## Eye liner

		contour = np.asarray(face['left_eye']).reshape(-1,1,2)
		#image = cv2.fillPoly(image,[contour], (60,70,70,2))
		image = cv2.polylines(image,[contour], True, (50,60,60),3)
		image = cv2.polylines(image,[contour], True, (0,0,0),2)
		image = cv2.addWeighted(image, 0.5, original, 0.5,0)
		

		original = image.copy()

		contour = np.asarray(face['right_eye']).reshape(-1,1,2)
		#image = cv2.fillPoly(image,[contour], (128,128,0))
		image = cv2.polylines(image,[contour], True, (50,60,60),3)
		image = cv2.polylines(image,[contour], True, (0,0,0),2)
		image = cv2.addWeighted(image, 0.5, original, 0.5,0)
		

		original = image.copy()

		contour = np.asarray(face['top_lip']).reshape(-1,1,2)
		image = cv2.fillPoly(image,[contour], (0,0,130))
		image = cv2.addWeighted(image, 0.6, original, 0.4,0)
		image = cv2.polylines(image,[contour], True, (0,0,150),2)

		original = image.copy()

		contour = np.asarray(face['bottom_lip']).reshape(-1,1,2)
		image = cv2.fillPoly(image,[contour], (0,0,130))
		image = cv2.addWeighted(image, 0.6, original, 0.4,0)
		image = cv2.polylines(image,[contour], True, (0,0,150),2)


cv2.imwrite(saving_dir, image)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
