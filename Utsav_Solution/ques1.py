import cv2
import os
from os import listdir
import pickle
# upadted twice

def store_coordinates(coord_list):
   for i,cood in enumerate(coord_list):
      dbfile = open(str(i), 'ab')
      pickle.dump(cood, dbfile)
      dbfile.close()

def load_coordinates(pickle_file):
   dbfile = open(pickle_file, 'rb')
   coord_list = pickle.load(dbfile)



dataset_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset'


cood = []
for path in listdir(dataset_folder):
   if (path.endswith(".jpeg")):
      print('Press 1 to proceed to next image....')
      k = input()
      if k == '1':
         print('Create bounding box....')

      img_path = "/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset/" + path
      img = cv2.imread(img_path)
      img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



      img_ini = img.copy()
      drawing = False
      ix,iy = -1,-1



      def draw_rectangle(event, x, y, flags, param):
         global ix, iy, drawing, img
         if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
            ix = x
            iy = y
         elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            cv2.rectangle(img, (ix, iy),(x, y),(0, 0, 0),3)
            cood.append(((ix,iy),(x,y)))


      cv2.namedWindow("Rectangle Window")

      cv2.setMouseCallback("Rectangle Window", draw_rectangle)

      while True:
         cv2.imshow("Rectangle Window", img)
         if cv2.waitKey(1) == ord('q'):
            break
         if cv2.waitKey(1) == ord('r'):
            img = img_ini
      print('destroying windows...')
      cv2.destroyAllWindows()




   else:
      print('format not matching')






print(cood)
store_coordinates(cood)