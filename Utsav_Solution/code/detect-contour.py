import cv2
import numpy as np


def findMaxContours(contours):
    span = []
    contour_y = [[]] * len(contours)
    for i, contour in enumerate(contours):
        ys = []
        for j in contour:
            ys.append(j[0][1])
        contour_y[i] = ys

    for ys in contour_y:
        if (len(ys) == 4):
            span.append(0)
        else:
            span.append(max(ys) - min(ys))
            max_height = max(span)
    print(span)
    return max_height, span.index(max_height)


dataset = "/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/data/"

img = cv2.imread(dataset + "shortvstall.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

max_height, contour_index = findMaxContours(contours)

# Find the tallest contour
# tallest_contour = max(contours, key=cv2.contourArea)

# # Draw the contour on the image
cv2.drawContours(img, contours, contour_index, (0, 255, 0), 2)

# # Show the result
cv2.imshow("Tallest Person", img)
cv2.waitKey(0)
cv2.destroyAllWindows()