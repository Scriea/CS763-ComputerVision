import cv2
import argparse

parser = argparse.ArgumentParser(prog='detectContour',
                                 description='Detects edges present in the image',
                                 )

parser.add_argument('-i', '--path', help='Takes path of the directory containing images')

args = parser.parse_args()

image_loc = r"{}".format(args.path)

img = cv2.imread(image_loc)

# these threshold values are found by hit and trial method
lower_thresh = 220
upper_thresh = 250

canny_img = cv2.Canny(img, lower_thresh, upper_thresh)
cv2.imshow('Canny image', canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()