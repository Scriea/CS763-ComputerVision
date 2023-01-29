import cv2
import os
from os import listdir
import pickle

def store_coordinates(coord_list, j):
   with open('/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/pickle_files/' + str(j), 'ab') as f:
      pickle.dump(coord_list, f)
   f.close()

def load_coordinates(pickle_file):
   dbfile = open(pickle_file, 'rb')
   coord_list = pickle.load(dbfile)
   return coord_list


dataset_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset'


cood = []
for j, path in enumerate(listdir(dataset_folder)):
   if (path.endswith(".jpeg")):
      print('Press p to proceed to next image....')
      k = input()
      if k == 'p':
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
            cood.append([ix,iy,x,y])


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

      store_coordinates(cood, j)
      cood = []

   else:
      print('format not matching')


saving_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/Blurred_images/'
pickle_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/pickle_files'


print(listdir(dataset_folder))
print(listdir(pickle_folder))


def Gaussian_Blur(dataset_folder, saving_folder, pickle_folder):
   i = 0
   data_list = listdir(dataset_folder)
   pic_list = listdir(pickle_folder)

   if '.DS_Store' in data_list:
      data_list.remove('.DS_Store')
   if '.DS_Store' in pic_list:
      pic_list.remove('.DS_Store')

   print(listdir(dataset_folder))
   print(listdir(pickle_folder))

   for path in data_list:

      img_path = "/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset/" + path
      print(img_path)

      # if (pic_lis[i].__contains__('.DS_Store')):
      #    i += 1
      #    continue
      print(pickle_folder + '/' + pic_list[i])
      coord_list = load_coordinates(pickle_folder + '/' + pic_list[i])
      i += 1
      img = cv2.imread(img_path)

      print(coord_list)


      result_img = img.copy()
      cv2.imshow('res img', result_img)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

      result_img[coord_list[0][1]:coord_list[0][3], coord_list[0][0]:coord_list[0][2],:] = cv2.GaussianBlur(result_img[coord_list[0][1]:coord_list[0][3], coord_list[0][0]:coord_list[0][2], :], (53, 53), 10000)

      cv2.imwrite(saving_folder + str(i) + '.jpg', result_img)
      print('saving resultant image...')

Gaussian_Blur(dataset_folder, saving_folder, pickle_folder)