import numpy as np
from PIL import Image
import cv2
import os

#extension of the files that are to be encoded to .npy
#or
#extension of the files that are to be decoded from .npy
IMAGE_FORMAT = ".png"

#name of the resulted encoded file
#or
#name of the file to decode from
IMAGES_AS_NPY_FILE_NAME = "images_as_npy.npy"

def main():
    encode_pictures_to_npy(IMAGE_FORMAT, IMAGES_AS_NPY_FILE_NAME)
    decode_npy_to_pictures(IMAGE_FORMAT, IMAGES_AS_NPY_FILE_NAME)

def encode_pictures_to_npy(image_format: str, file_name: str):
    #get a list of all the files in the current directory
    #which end in the proper extension
    image_names = filter(lambda image_name: image_name[-len(image_format):] == image_format, os.listdir())

    #initalize with an empty numpy array
    result_npy_array = []

    for image_name in image_names:
        result_npy_array.append(                                            #add to the array
            cv2.cvtColor(cv2.imread(image_name, cv2.IMREAD_UNCHANGED),      #the image, converted into a numpy array
                        cv2.COLOR_BGRA2RGBA)                                  #color scheme so it doesnt get inverted
        )

    #finally, save the result array as a file
    np.save(file_name, result_npy_array)


def decode_npy_to_pictures(image_format: str, file_name: str):
    #get the .npy file as an array
    img_array = np.load(file_name, allow_pickle=True)
    x = 1
    for img in img_array:                               #iterate over each image inside the .npy file
        im = Image.fromarray(img)                       #get each image as an array
        im.save("img" + str(x) + image_format)          #save it as an actual image
        x += 1

if __name__ == "__main__":
    main()