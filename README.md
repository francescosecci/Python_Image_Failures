# Python Image Failures

In questa repository sono contenuti dei codici che servono per simulare fallimenti che possono verificarsi su delle immagini.

I codici sono stati trovati e modificati, in modo da essere ottimali per il lavoro che doveva essere svolto.


## Alcune cose su codice utilizzato

Per la conversione da 'PIL.JpegImagePlugin.JpegImageFile' (o 'PIL.Image.Image') a 'numpy.ndarray' si può usare il comando:
```python
img1 = np.array(picture) # adesso img1 è un oggetto <class 'numpy.ndarray'>
```

Per la conversione opposta, ovvero da 'numpy.ndarray' a 'PIL.Image.Image' si può usare il comando: 
```python
img1 = Image.fromarray(blur, 'RGB') # adesso img1 è un oggetto <class 'PIL.Image.Image'>
```

Se l'oggetto 'ndarray' dell'immagine letta da OpenCV col metodo cv2.imread() viene convertito in a un oggetto 'PIL.Image' 
e salvato, l'immagine risulterà con colori sbagliati (canali R e B invertiti), dunque, nei codici caricati, si è spesso 
utilizzato il comando:
```python
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR to RGB
```
