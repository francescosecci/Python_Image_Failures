# Python Image Failures

In questa repository sono contenuti dei codici che servono per simulare fallimenti che possono verificarsi in una fotocamera/videocamera in fase di acquisizione/elaborazione.

I codici sono stati trovati e modificati, in modo da essere ottimali per il lavoro che doveva essere svolto.


## Alcune cose sul codice utilizzato

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


## Risultati ottenuti con l'iniezione dei fallimenti in CARLA

I Success Rate della Golden Run:

| \/\\\/\\\/\\\/\\\/\\ | FullTown02 | StraightTown02 | TurnTown02 |
| ------------- | ------------- | ------------- | ------------- |
| GoldenRun | 90 | 100 | 100  |


I Success Rate dei fallimenti iniettati:

| Failure's name | FullTown02 | StraightTown02 | TurnTown02 |
| ------------- | ------------- | ------------- | ------------- |
| NONOISE1 | 76  | 100  | 98  |
| NONOISE2 | 16  | 90  | 40  |
| BLUR | 6  | 82  | 40  |
| BRIGH1 | 76  | 98  | 96  |
| BRIGH2 | 18  | 78  | 48  |
| WHI | 0  | 10  | 0  |
| BLA | 0  | 12  | 0  |
| BRLE1 | 0  | 22  | 8  |
| BRLE2 | 38  | 96  | 74  |
| NBAYF | 74  | 98  | 98  |
| NOSHARP | 80  | 100  | 86  |
| NOCHROMAB-nb | 52  | 96  | 76  |
| NOCHROMAB-b | 32  | 92  | 60  |
| ICE1 | 60  | 98  | 90  |
| ICE2 | 2  | 86  | 8  |
| DIRTY1 | 76  | 100  | 98  |
| DIRTY2 | 34  | 98  | 70  |
| RAIN | 66  | 100  | 92  |
| COND | 32  | 94  | 84  |
| BAND | 90  | 100  | 96  |
| NODEMOS | 78  | 98  | 88  |
| DEAPIX1 | 90  | 98  | 100  |
| DEAPIX50 | 80  | 98  | 98  |
| DEAPIX200 | 74  | 100  | 100  |
| DEAPIX1000 | 74  | 100  | 98  |
| DEAPIX-vcl | 82  | 100  | 98  |
| DEAPIX-3l | 68  | 100  | 92  |
| DEAPIX-5l | 52  | 96  | 90  |
| DEAPIX-10l | 70  | 94  | 98  |
| DEAPIXl-r | 40  | 100  | 68  |
| DEAPIX-ro | 36  | 100  | 70  |
| Media Success Rate per Scenario (GoldenRun inclusa) | 51.94 % | 88.56 % | 73.81 % |


## Immagini esempio fallimenti

Frame CARLA senza iniezione di Fallimenti
<img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/originale.jpg" width="250">
