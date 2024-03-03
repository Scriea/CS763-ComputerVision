import cv2
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser(prog='detectContour',
                                 description='Creates contour over the tallest guy in the picture',
                                 )
parser.add_argument('-i', "--path", help='Takes path of the directory containing images')

args = parser.parse_args()

image_loc = r"{}".format(args.path)


def findMaxContours(contours):
    span = []
    contour_y = [[]] * len(contours)
    for i, contour in enumerate(contours):
        ys = []
        for j in contour:
            ys.append(j[0][1])
        contour_y[i] = ys

    for ys in contour_y:
        if (len(ys) < 10):
            span.append(0)
        else:
            span.append(max(ys) - min(ys))
            max_height = max(span)
    return max_height, span.index(max_height)


img = cv2.imread(image_loc)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_height, contour_index = findMaxContours(contours)

cv2.drawContours(img, contours, contour_index, (0, 255, 0), 2)

# # Show the result
cv2.imshow("Tallest Person", img)
cv2.waitKey(0)
cv2.destroyAllWindows