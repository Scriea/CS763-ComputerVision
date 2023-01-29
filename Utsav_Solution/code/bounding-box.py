# Some important imports
import cv2
import os
from os import listdir
import pickle


# functions to store coordinates of a bounding box in a pickle file
def store_coordinates(coord_list, j):
    with open('/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/pickle_files/' + str(j), 'wb') as f:
        pickle.dump(coord_list, f)
    f.close()


# load coordinates from a pickle file in a list
def load_coordinates(pickle_file):
    dbfile = open(pickle_file, 'rb')
    coord_list = pickle.load(dbfile)
    return coord_list


# defining some important folder paths to be used later in the code
dataset_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset/bounding-box'
saving_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/Utsav_Solution/results-bounding-box/'
pickle_folder = '/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/pickle_files'

# main for loop to get annotation inputes from the user
# proceed according to the instructions in the output box
cood = []
for j, path in enumerate(listdir(dataset_folder)):
    if path.endswith(".jpeg"):
        print('Press p to proceed to next image....')
        k = input()
        if k == 'p':
            print('Please drag and drop to draw a box and press q after creating required boxes')

        img_path = "/Users/utsavmdesai/Documents/SEM 6/CS 763/Task1/Solution/dataset/bounding-box/" + path
        img = cv2.imread(img_path)
        img_plt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_ini = img.copy()
        drawing = False
        ix, iy = -1, -1


        def draw_rectangle(event, x, y, flags, param):
            global ix, iy, drawing, img
            if event == cv2.EVENT_LBUTTONDOWN:
                drawing = True
                ix = x
                iy = y
            elif event == cv2.EVENT_LBUTTONUP:
                drawing = False
                cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 3)
                cood.append([ix, iy, x, y])


        cv2.namedWindow("Rectangle Window")

        cv2.setMouseCallback("Rectangle Window", draw_rectangle)

        while True:
            cv2.imshow("Rectangle Window", img)
            if cv2.waitKey(1) == ord('q'):
                break
            if cv2.waitKey(1) == ord('r'):
                img = img_ini
        cv2.destroyAllWindows()

        store_coordinates(cood, j)
        cood = []

    else:
        print('format not matching')  # format other than the one specified above


# fucntion to apply blur inside the bounding box
def Gaussian_Blur_Rectangle(dataset_folder, saving_folder, pickle_folder):
    i = 0
    data_list = listdir(dataset_folder)
    pic_list = listdir(pickle_folder)

    # if conditions to check for '.DS_Store' file in the lists(useful for mac users)
    if '.DS_Store' in data_list:
        data_list.remove('.DS_Store')
    if '.DS_Store' in pic_list:
        pic_list.remove('.DS_Store')

    for path in data_list:
        img_path = dataset_folder + "/" + path
        coord_list = load_coordinates(pickle_folder + '/' + pic_list[i])
        i += 1
        img = cv2.imread(img_path)

        result_img = img.copy()

        for k in range(len(coord_list)):
            result_img[coord_list[k][1]:coord_list[k][3], coord_list[k][0]:coord_list[k][2], :] = cv2.GaussianBlur(
                result_img[coord_list[k][1]:coord_list[k][3], coord_list[k][0]:coord_list[k][2], :], (53, 53), 10000)
            result_img = cv2.rectangle(result_img, (coord_list[k][0], coord_list[k][1]),
                                       (coord_list[k][2], coord_list[k][3]), (0, 0, 0), 2)

        cv2.imwrite(saving_folder + str(i) + '.jpg', result_img)
        print('Final image saved at ' + saving_folder)


Gaussian_Blur_Rectangle(dataset_folder, saving_folder, pickle_folder)
