import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sim.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Speckle Noise
#second value (the "1") is the Standard deviation (spread or "width") of the distribution 
gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
noise = img + img * gauss

plt.figure(num='Fallimento NOISE')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(noise),plt.title('Noise')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
