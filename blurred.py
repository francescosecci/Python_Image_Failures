#add blur to the image sim1.jpg
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sim1.jpg')

blur = cv2.blur(img,(5,5)) #change values to increment/decrement blur. 0 is "no blur"

#blur e img --> <class 'numpy.ndarray'>

#il codice sotto serve come presentazione per mostrare il fallimento
plt.figure(num='Fallimento BLURRED')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Sfocata')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
