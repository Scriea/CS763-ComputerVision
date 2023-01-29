import cv2

image_path = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset/edges/butterfly.jpg'

img = cv2.imread(image_path)

# cv2.imshow('Input image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#these threshold values are found by hit and trial method
lower_thresh = 220
upper_thresh = 250


canny_img = cv2.Canny(img, lower_thresh ,upper_thresh)
cv2.imshow('Canny image', canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()