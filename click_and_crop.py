
import cv2
import numpy as np
import os
 
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPoint, image, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being

    
    # Mouse is Moving
    if event == cv2.EVENT_MOUSEMOVE:
        image = image_original.copy()
        # define refPoint
        tl_x = w-crop_size if x > w-crop_size//2 else max(0, x-crop_size//2) # to confine in image
        tl_y = h-crop_size if y > h-crop_size//2 else max(0, y-crop_size//2) # to confine in image
        br_x = tl_x + crop_size
        br_y = tl_y + crop_size
        refPoint = [(tl_x,tl_y),(br_x, br_y)]
        # draw ractangle
        cv2.rectangle(image, (refPoint[0][0], refPoint[0][1]), (refPoint[1][0], refPoint[1][1]), (255, 0, 0), 2)

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        cropping = True

    return


######################################################
#####                PARAMETERS                  #####
######################################################
cropping = False
print("Image Directory Path : ")
img_path = input()
print("Crop size :")
crop_size = input()
crop_size = int(crop_size)
#img_path = 'D:\\Dataset\\WHTM_PH2_Mask_1\\review image\\PO03\\'
img_list = os.listdir(img_path)
img_list = [i for i in img_list if i.endswith('.jpg') or i.endswith('.bmp')]
print(img_list)
print()
print("Crop size :", end="\r")


cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 800,800)
cv2.setMouseCallback("image", mouse_crop)

new_crop_size = ""

for j in range(len(img_list)):

    image = cv2.imread(os.path.join(img_path,img_list[j]))
    h, w, _ = np.shape(image)
    image_original = image.copy()
    oriImage = image.copy()
    cropping = False
    cnt = 0
    while True:
        #i = image.copy()
        if not cropping:
            cv2.imshow("image", image)
        elif cropping:
            cv2.imshow("image", image)
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imwrite("..\\crop\\{}_crop.bmp".format(img_list[j][:-4]), roi)
            break

        k = cv2.waitKey(1)
        if k>=48 and k<=57: # numbers
            if new_crop_size == "":
                new_crop_size = chr(k)
            else:
                new_crop_size += chr(k)
            #print(new_crop_size)
        elif k == 8: # backspace
            new_crop_size = new_crop_size[:-1]
            #print(new_crop_size)
        elif k == 13: # enter
            crop_size = int(new_crop_size)
            print("Crop size : ", crop_size, end="\r")
            new_crop_size = ""
            


 
# close all open windows
cv2.destroyAllWindows()