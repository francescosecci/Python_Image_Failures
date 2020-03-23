import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt

img = cv2.imread('sim1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = Image.open('sim1.jpg').convert('LA')
# in alcuni casi .convert('LA') potrebbe non funzionare e l'altra conversione
# che ho utilizzato è .convert('L')

plt.figure(num='Fallimento NO BAYER FILTER')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gray),plt.title('Scala di Grigi')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
