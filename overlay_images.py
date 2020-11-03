#It allow to overlay images without losing brightness, if the foreground image is transparent
#The "overlay" is our approach to banding, rain, condensation, broken lens, ice, dirt failures.
#The github contains some images that you can overlay to sim1.jpg, but others obviously exist.

from matplotlib import pyplot as plt
from PIL import Image
import os
import cv2



img = Image.open("sim1.jpg")
img3 = Image.open("sim1.jpg")
#this works nice if the image to be overlayed (the foreground image, ice3.png in this case) is transparent
img2 = Image.open("./ice/ice3.png").convert("RGBA")
img3.paste(img2, (0, 0), img2)

#Alternative approach, if foreground image is not transparent:
#essenzially resize, blend, then add brightness to get as close as possible to the original image.

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
