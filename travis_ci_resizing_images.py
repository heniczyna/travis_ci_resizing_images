#Resized image is 25% of the original size
#
#Put this script in your favourite directory
#In chosen directory create an additional folder called "to_resize" with images to resize (.\to_resize)
#Run the script
#
#Python 3.7.2 64-bit

import os
import cv2

dir_path = os.getcwd()
print("Current working directory is: ", dir_path)
#could be also:
#print("Current working directory is: ", os.getcwd())

img_to_resize_path = os.path.join(dir_path, "to_resize")
print("Directory with images to resize is: ", img_to_resize_path)

dir_list = os.listdir(img_to_resize_path)
print("List of images in directory with images to resize is: ", dir_list)
#could be also:
#print("List of images in directory with images to resize is: ", os.listdir(img_to_resize_path))

#Change the current directory to save resized images in the same directory as original images
#Resized images will have "resized_" prefix
os.chdir(img_to_resize_path)

counter = 0 #to check how many files have been resized

for filename in dir_list:
    #If the images are not .jpg images, change the line below to match the image type
    #Be aware that jpg is not equal to JPG
    if filename.endswith(".jpg"):
        print("Read image is: ", filename)
        counter += 1
        image = cv2.imread(filename)
        resized = cv2.resize(image, None, fx = 0.25, fy = 0.25, interpolation = cv2.INTER_AREA)
        cv2.imwrite("resized_" + filename, resized)
print("Number of files: ", counter)