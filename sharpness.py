from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt

'''
Sharpness: This class can be used to adjust the sharpness
of an image. An enhancement factor of 0.0 gives a
blurred image, a factor of 1.0 gives the original
image, and a factor of 2.0 gives a sharpened image.
'''

img = Image.open("sim1.jpg") #se apri l'immagine con Image.open() non ci sono problemi
                             # con i canali dei colori, se invece usi cv2.imread()
                             # devi usare cv2.cvtColor(img, cv2.COLOR_BGR2RGB) per avere
                             # colori corretti

enhancer = ImageEnhance.Sharpness(img)

factor = 1
img1 = enhancer.enhance(factor)

'''

esempi:

factor = 1 --> img Originale
factor = 3 --> img visibilmente più definita (non sempre un bene)
factor = -3.5 --> img sfocata, non nitida (si avvicina molto al guasto Blurred)

'''

factor = -3.5
img2 = enhancer.enhance(factor)


plt.figure(num='Fallimento SHARPNESS')
plt.subplot(121),plt.imshow(img1),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('Sharpened')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
