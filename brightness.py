from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt

'''
Brightness: This class can be used to control the
brightness of an image. An enhancement
factor of 0.0 gives a black image.
A factor of 1.0 gives the original image.
'''


img = Image.open("sim1.jpg")

enhancer = ImageEnhance.Brightness(img)

factor = 1
img1 = enhancer.enhance(factor)


factor = 3.5
img2 = enhancer.enhance(factor)

# img --> <class 'PIL.JpegImagePlugin.JpegImageFile'>
# img1 e img2 --> <class 'PIL.Image.Image'>

plt.figure(num='Fallimento BRIGHTNESS')
plt.subplot(121),plt.imshow(img1),plt.title('Originale')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('Luminosità Aumentata')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
