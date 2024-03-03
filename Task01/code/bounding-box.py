import cv2
import os
from os import listdir
import pickle
import argparse
import sys

'''
## Comments are not addded in code. For detailed explations read ReflectionEssay.pdf !!

'''

## Parser
parser = argparse.ArgumentParser(prog='detectContour',
                                 description='To annotate faces present in images and videos',
                                 )

parser.add_argument('-d', '--data', required=True, help='Takes path of the directory containing images or video')
parser.add_argument('-a', '--annotation', required=True, help='Takes path of the directory to save annotation')
parser.add_argument('-t', '--type', required=True, type=int, help='Defines which operation to perform')

args = parser.parse_args()

img = None
img_list = []


## Directories
dataset_folder = r"{}".format(args.data)  + "\\"
pickle_folder = r"{}".format(args.annotation)  + "\\"
results_folder = r"{}".format(os.path.dirname(os.getcwd()) + "\\results\\")
print(results_folder)


## Functions
def store_coordinates(coord_list, basename, pickle_folder):
    with open(pickle_folder + basename + '.txt', 'wb') as f:
        pickle.dump(coord_list, f)
    f.close()


def load_coordinates(pickle_file):
    dbfile = open(pickle_file, 'rb')
    coord_list = pickle.load(dbfile)
    return coord_list


def Gaussian_Blur(dataset_folder, pickle_folder):
    i = 0
    print("press any key to proceed")
    for path in listdir(dataset_folder):
        if (path.endswith((".jpeg", ".png", ".jpg"))):
            img_path = dataset_folder + path
            pic_lis = listdir(pickle_folder)
            coord_list = load_coordinates(pickle_folder + listdir(pickle_folder)[i])
            i = i + 1
            img = cv2.imread(img_path)
            result_img = img.copy()

            for k in range(len(coord_list)):
                result_img[coord_list[k][1]:coord_list[k][3], coord_list[k][0]:coord_list[k][2], :] = cv2.GaussianBlur(
                    result_img[coord_list[k][1]:coord_list[k][3], coord_list[k][0]:coord_list[k][2], :],
                    (53, 53), 10000)
                cv2.rectangle(result_img, (coord_list[k][0], coord_list[k][1]), (coord_list[k][2], coord_list[k][3]),
                              (0, 0, 0), 3)

            basename = str(path.split(".")[0])
            cv2.imshow('res img', result_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    print("Task executed!")


drawing = False
ix, iy = -1, -1
cood = []
cood_v = []


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, cood
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        ix, x = min(ix, x), max(ix, x)
        iy, y = min(iy, y), max(iy, y)
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 0), 3)
        cood.append([ix, iy, x, y])


def iterate_image(dataset_folder, pickle_folder):  
    annotated_img = []
    i = 0
    for path in listdir(dataset_folder):
        if (path.endswith((".jpeg", ".png", ".jpg"))):
            img_path = dataset_folder + path
            print(img_path)
            pic_lis = listdir(pickle_folder)
            coord_list = load_coordinates(pickle_folder + '/' + listdir(pickle_folder)[i])
            i = i + 1
            img = cv2.imread(img_path)
            result_img = img.copy()

            for k in range(len(coord_list)):
                cv2.rectangle(result_img, (coord_list[k][0], coord_list[k][1]), (coord_list[k][2], coord_list[k][3]),
                              (0, 0, 0), 3)
            annotated_img.append(result_img)
    b = 0
    l = len(annotated_img)
    while True:
        cv2.imshow("Image", annotated_img[b])
        if cv2.waitKey(20) == ord('p'):
            b = (b - 1) % l
        elif cv2.waitKey(20) == ord('n'):
            b = (b + 1) % l
        elif cv2.waitKey(20) == ord('q'):
            break
        else:
            continue
    print("Task executed!")


def image_func(dataset_folder, pickle_folder):
    global img, cood
    print("Press p to proceed !")
    for j, path in enumerate(listdir(dataset_folder)):
        if (path.endswith(".jpeg") or path.endswith(".png")):
            # print('Press p to proceed to next image....')
            # k = input()
            # if k == 'p':
            #     print('Create bounding box....')

            img_path = dataset_folder + path
            img = cv2.imread(img_path)
            img_ini = img.copy()

            cv2.namedWindow("Rectangle Window")

            cv2.setMouseCallback("Rectangle Window", draw_rectangle)

            while True:
                cv2.imshow("Rectangle Window", img)
                if cv2.waitKey(50) == ord('p'):
                    break
                if cv2.waitKey(50) == ord('q'):
                    print("Ending Process !")
                    sys.exit()

            cv2.destroyAllWindows()

            store_coordinates(cood, str(path.split('.')[0]), pickle_folder)
            print("Storing Coordinates")
            cood = []
        else:
            print('format not matching i.e.(not .png, .jepg)')
    print("Task executed!")


def video_func(dataset_folder_video, pickle_folder_video):
    print("\n Starting video feed")
    global img, cood_v, cood
    cood = []
    for j, path in enumerate(listdir(dataset_folder_video)):
        if (path.endswith(".mp4")):
            cap = cv2.VideoCapture(dataset_folder_video + path)            ## Creating capture
            cap.set(cv2.CAP_PROP_FPS, 1)

            print('Press p to proceed to next image....')
            k = input()
            if k == 'p':
                print('Create bounding box....')

            ## reading frames
            while True:
                ret, img = cap.read()
                if not ret:
                    break

                # Display the resulting frame
                cv2.namedWindow("Rectangle Window")
                cv2.setMouseCallback("Rectangle Window", draw_rectangle)

                while True:
                    cv2.imshow("Rectangle Window", img)
                    if cv2.waitKey(50) == ord('p'):
                        break
                # print('destroying windows...')
                cv2.destroyAllWindows()

                cood_v.append(cood)
                cood = []
                # cv2.waitKey(200)
                if cv2.waitKey(10) == ord('q'):
                    break
            print("Storing Coordinates")
            store_coordinates(cood_v, path.split(".")[0], pickle_folder_video)
            ## print(cood_v)

            cap.release()
            cv2.destroyAllWindows()
    print("Task executed!")


def Gaussian_Blur_video(dataset_folder_video, saving_folder_video, pickle_folder_video):
    for j, path in enumerate(listdir(dataset_folder_video)):
        if (path.endswith('.mp4')):
            cap = cv2.VideoCapture(dataset_folder_video + path)
            cap.set(cv2.CAP_PROP_FPS, 1)
            coord_list = load_coordinates(pickle_folder_video + listdir(pickle_folder)[j])
            i = 0
            while True:
                ret, img = cap.read()
                if not ret:
                    # print("Can't receive frame (stream end?). Exiting ...")
                    break
                result_img = img.copy()

                for k in range(len(coord_list[i])):
                    result_img[coord_list[i][k][1]:coord_list[i][k][3], coord_list[i][k][0]:coord_list[i][k][2],
                    :] = cv2.GaussianBlur(
                        result_img[coord_list[i][k][1]:coord_list[i][k][3], coord_list[i][k][0]:coord_list[i][k][2], :],
                        (53, 53), 10000)
                    cv2.rectangle(result_img, (coord_list[i][k][0], coord_list[i][k][1]),
                                  (coord_list[i][k][2], coord_list[i][k][3]), (0, 0, 0), 3)
                img_list.append(result_img)
                i += 1
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            cap.release()
            cv2.destroyAllWindows()

            img_shape = img_list[0].shape[1], img_list[0].shape[0]
            out = cv2.VideoWriter(saving_folder_video + path.split('.')[0] + '.mp4', cv2.VideoWriter_fourcc(*'mp4v'),
                                  3.0, img_shape)

            for image in img_list:
                out.write(image)
                print('saved to video')
            out.release()

    print("Task executed!")


if (args.type == 1):
    image_func(dataset_folder, pickle_folder)

elif (args.type == 2):
    iterate_image(dataset_folder, pickle_folder)
elif (args.type == 3):
    Gaussian_Blur(dataset_folder, pickle_folder)

elif (args.type == 4):
    video_func(dataset_folder, pickle_folder)

elif (args.type == 5):
    Gaussian_Blur_video(dataset_folder, results_folder, pickle_folder)
else:
    print("Incorrect type!")

print("*_______________*")