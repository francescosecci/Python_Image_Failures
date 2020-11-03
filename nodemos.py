#adds the "no demosaicing failure" on input image sim1.jpg 
from PIL import Image
from numpy import*
import cv2
from matplotlib import pyplot as plt

# Open image and put it in a numpy array
srcArray = cv2.imread('sim1.jpg')
srcArray1 = Image.open("sim1.jpg")

w, h, _ = srcArray.shape
# Create target array, twice the size of the original image
resArray = zeros((2*w, 2*h, 3), dtype=uint8)

# Map the RGB values in the original picture according to the BGGR pattern#

# Blue
resArray[::2, ::2, 2] = srcArray[:, :, 2]

# Green (top row of the Bayer matrix)
resArray[1::2, ::2, 1] = srcArray[:, :, 1]

# Green (bottom row of the Bayer matrix)
resArray[::2, 1::2, 1] = srcArray[:, :, 1]

# Red
resArray[1::2, 1::2, 0] = srcArray[:, :, 0]

resArray = cv2.cvtColor(resArray, cv2.COLOR_BGR2RGB)
# Save the image
imgOut = Image.fromarray(resArray, "RGB")
#imgOut = imgOut.resize((h,w), Image.ANTIALIAS)#se usi questo comando non vedrò
                                               #i pixel distinti in R, G e B pixels
                                               # con predominanza di pixel G, ma
                                               #risulterà un'immagine verdastra
                                               #della stessa dim. dell'Originale
                                               #(non è proprio quello che si
                                               #vuole ottenere da questo effetto)
# Save the image
# imgOut.save("nodemos.png")

plt.figure(num='Failure DEMOSAICING')
plt.subplot(121),plt.imshow(srcArray1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgOut),plt.title('No Demosaicing')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
