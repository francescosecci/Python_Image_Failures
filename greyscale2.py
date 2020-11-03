import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import os

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


#2 approaches for transforming in greyscale
#see greyscale.py and this file greyscale2.py
#depending on your image detection algorithm, one or the other may be preferable
img = mpimg.imread('sim1.jpg')
gray = rgb2gray(img)

plt.figure(num='Failure NO BAYER FILTER')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gray),plt.title('Greyscale')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
