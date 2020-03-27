
import cv2
import numpy as np
import os
 
cropping = False
cropping_up = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0
 
img_path = 'D:\\Dataset\\[Project]_HKC_H5_SAMPLE_TEST_IMAGE\\training_data_rescaling\\F8XPP_195_PS_Defect\\low\\none\\'
img_list = os.listdir(img_path)
img_list = [i for i in img_list if i[-1] == 'g']

image = cv2.imread('D:\\temp_crop_test\\test.jpg')
print("hello")
print(type(image))
oriImage = image.copy()

roi_g = 1
 
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
 
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
 
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
 
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        x_one, y_one = x, y

        cropping = False # cropping is finished
 
        refPoint = [(x_start, y_start), (x_end, y_end)]
        refPoint2 = [(x-149,y-149),(x+150,y+150)]
 
        if len(refPoint) == 2: #when two points were found
            roi = oriImage[refPoint2[0][1]:refPoint2[1][1], refPoint2[0][0]:refPoint2[1][0]]
            
            cv2.imshow("Cropped", roi)

            
            
 
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("image", 800,800)
cv2.setMouseCallback("image", mouse_crop)
 
#while True:
 
#    i = image.copy()
 
#    if not cropping:
#        cv2.imshow("image", image)
 
#    elif cropping:
#        cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
#        cv2.imshow("image", i)

 
#    cv2.waitKey(1)


for j in range(len(img_list)):

    image = cv2.imread(img_path + img_list[j])
    
    oriImage = image.copy()

    cropping = False
    

    while True:
 
        i = image.copy()
 
        if not cropping:
            cv2.imshow("image", image)
 
        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.imshow("image", i)

            refPoint2 = [(x_end-149,y_end-149),(x_end+150,y_end+150)]
            roi = oriImage[refPoint2[0][1]:refPoint2[1][1], refPoint2[0][0]:refPoint2[1][0]]

            cv2.imwrite("..\\crop\\{}_crop.jpg".format(img_list[j][:-4]), roi)

            break
 
        cv2.waitKey(1)

        
 
# close all open windows
cv2.destroyAllWindows()