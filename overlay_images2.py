#see overlay_images.py for an alternative (better) method
#Overlay is our approach to banding, rain, condensation, broken lens, ice, dirt.
#The github contains some images that you can overlay to sim1.jpg, but many others obviously can be used.

from matplotlib import pyplot as plt
from PIL import Image


img = Image.open("sim1.jpg")

img2 = Image.open("broken1.png").convert(img.mode) # broken1.png is overlayed to sim1.jpg
# pay attention that it may get the image darker
# see overlay_images.py for alternatives

img2 = img2.resize(img.size)

img3 = Image.blend(img,img2,0.35)#valori per immagine banding->0.02, banding1->0.05, ice->0.2

plt.figure(num='Fallimento BROKEN LENS')
plt.subplot(121),plt.imshow(img),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3),plt.title('Broken Lens')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
