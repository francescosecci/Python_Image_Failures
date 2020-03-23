import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image


img = cv2.imread('sim1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
'''
If the 'ndarray' of the image read by OpenCV imread() is converted to a
'PIL.Image' object and saved, the image with the wrong color is saved.

If you want to convert 'ndarray' and 'PIL.Image' objects to use both Pillow
and OpenCV functions, you need to convert BGR and RGB.
'''

img1 = Image.open('sim1.jpg')

pixels = img1.load()

width, height = img1.size

for i in range(0, width):
    for j in range(0, height):
        if i==150 and j==90:
            pixels[i,j] = (255,0,0) # rosso per notarlo meglio nell'immagine

img1 = np.array(img1) # esempio trasformazione da PIL.JpegImagePlugin.JpegImageFile
                      # a 'numpy.ndarray'

plt.figure(num='Fallimento DEADPIXEL')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DeadPixel')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
