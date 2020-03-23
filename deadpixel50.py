import numpy as np
import cv2
from matplotlib import pyplot as plt
import random

img = cv2.imread('sim1.jpg')

img1 = cv2.imread('sim1.jpg')

h, w, _ = img1.shape

count = 0
w1 = w2 = int((w-70)/10) # in base a questo 10 e al 5 sotto decido quanti pixel neri inserire
h1 = h2 = int((h-70)/5)
w2 = w3 = w2 - 5
h2 = h3 = h2 - 5
countpixel = 0

# naturalmente bisogna sempre controllare con un paio di prove (o calcolandolo)
# se si esce confini dell'immagine in elaborazione

for y in range(0, 5):
    h2 = h2 + (h1*y)
    for x in range(0, 10):
        #print("h2 e w2: " + str(h2) +" e "+ str(w2))
        #inserimento di randomicità per quanto riguarda
        #le coordinate in cui vengono posti i pixel neri (in fase sperimentale
        #considerato un valore fisso, in quanto deve essere replicabile e quindi
        #sempre uguale):
        #  img1[(h2+random.randint(1,20)),(w2+random.randint(1,20))] = (0, 0, 0)
        #versione per fase sperimentale sotto ("tutto fisso")
        img1[h2,w2] = (255, 0, 0) #pixels rossi (per visibilità) in coordinate [h2,w2]
        countpixel = countpixel + 1
        w2 = w2 + w1
        if x==9:
            h2 = h3
            w2 = w3


print(countpixel) #valore di controllo per l'inserimento del giusto numero
                  #di pixel neri

plt.figure(num='Fallimento DEADPIXEL Configurazione 2 - 50 pixel Neri')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DEADPIXEL - Configurazione 2')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
