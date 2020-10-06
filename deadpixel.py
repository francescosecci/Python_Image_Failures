import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image


img= cv2.imread('sim1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


img1 = cv2.imread('sim1.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
h, w, _ = img1.shape
#set  pixel at coordinates 90, 150 to black color
w=150
h=90
img1[h,w]=(0,0,0)
img1 = Image.fromarray(img1)


plt.figure(num='Fallimento DEADPIXEL')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DeadPixel')
plt.xticks([]), plt.yticks([])
plt.show()
