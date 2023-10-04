import cv2
import numpy as np

def filter_1(img):
    #filter number1
    return

def filter_2(img):
    #filter number 2
    return

def filter_3(img):
    #filter number 3
    return

filter_set = {
    1 : filter_1,
    2 : filter_2,
    3 : filter_3
}

number = int(input('Enter number of use filter'))

image = cv2.imread('my_image.jpg')

my_filter = filter_set[number]
result_image = my_filter(image)