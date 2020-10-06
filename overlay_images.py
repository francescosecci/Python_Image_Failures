#alternative metod to "sovrapposizione.py"
#allow to overlay images without losing brightness, if foreground image is transparent

from matplotlib import pyplot as plt
from PIL import Image
import os
import cv2



img = Image.open("sim.jpg")
img3 = Image.open("sim.jpg")
# attenzione a che tipo di sfondo hanno, in quanto potrebbero o dare errore o scurire
# talmente tanto l'immagine che non potrebbero essere considerati come plausibili
img2 = Image.open("./ice/ice3.png").convert("RGBA")
img3.paste(img2, (0, 0), img2)

#Alternative:

#img2 = Image.open("broken1.png").convert(img.mode) # immagini da sovrapporre all'Originale
#img2 = img2.resize(img.size)
#img3 = Image.blend(img,img2,0.35)#valori per immagine banding->0.02, banding1->0.05, ice->0.2
#then you can add some brightness
#enhancer = ImageEnhance.Brightness(img3)
#factor = 1.6 #choose a value
#img3 = enhancer.enhance(factor)

plt.figure(num='Overlay image')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3),plt.title('Overlaid image')
#plt.subplot(122),plt.imshow(img3),plt.title('Overlaid image')
plt.xticks([]), plt.yticks([])
plt.show()
