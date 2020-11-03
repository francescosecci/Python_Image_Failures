# Python Image Failures

This repository contains codes that are used to simulate failures that can occur in a camera during the acquisition/processing phase.

The codes were found and modified, so as to be optimal for the work that had to be done.

### If you are using our work, please cite:
Francesco Secci, Andrea Ceccarelli. "On failures of RGB cameras and their effects in autonomous driving applications." In: The 31st International Symposium on Software Reliability Engineering (ISSRE) 2020.

## How to interpret this code
There are various python files, and some images.
In general: 
- sim1.jpg is the target image, on which failures are applied
- each python file allows injecting a different failure on sim1.jpg. The name of the file itself indicates the failures:
   - some failures (banding, ice, condensation, dirt, rain, broken lens) requires a second image, that is overlapped on sim1.jpg. In these cases, some possible images are available in the repository (e.g., banding.png, ice1.png). Obviously, many others can be used.
   - other failures may have configuration parameters, you can play with them. It is easy to spot them just looking at the code and the comments. 

## Few things about the code used

For the conversion from 'PIL.JpegImagePlugin.JpegImageFile' (or 'PIL.Image.Image') to 'numpy.ndarray' you can use the command:
```python
img1 = np.array(picture) # now img1 is a <class 'numpy.ndarray'> object
```

For the opposite conversion (from 'numpy.ndarray' to 'PIL.Image.Image') you can use the command:
```python
img1 = Image.fromarray(blur, 'RGB') # now img1 is a <class 'PIL.Image.Image'> object
```

If the image is opened using the cv2.imread() method (OpenCV) and converted into a 'PIL.Image' object, saving it, it will have wrong colors: the R and B channels will be inverted, therefore, in the codes in the repository, the command below has often been used:
```python
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR to RGB
```

<br><br>
## Types of weather available in the simulator:

- [ ] 0 - Default 
- [x] 1 - ClearNoon
- [ ] 2 - CloudyNoon
- [ ] 3 - WetNoon
- [x] 4 - WetCloudyNoon
- [ ] 5 - MidRainyNoon
- [ ] 6 - HardRainNoon
- [ ] 7 - SoftRainNoon
- [ ] 8 - ClearSunset
- [ ] 9 - CloudySunset
- [ ] 10 - WetSunset
- [ ] 11 - WetCloudySunset
- [ ] 12 - MidRainSunset
- [x] 13 - HardRainSunset
- [ ] 14 - SoftRainSunset

The marked weather are those used in the work done.

<br><br>
## Results obtained with the injection of failures in CARLA simulator

Success Rate of Golden Run:

| \/\\\/\\\/\\\/\\\/\\ | FullTown02 | StraightTown02 | TurnTown02 |
| ------------- | ------------- | ------------- | ------------- |
| GoldenRun | 90 | 100 | 100  |


Success rates of injected failures:

| Failure name | FullTown02 | StraightTown02 | TurnTown02 |
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
| Average Success Rate per Scenario (GoldenRun included) | 51.94 % | 88.56 % | 73.81 % |

<br><br>
## Examples of failures injected

| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/originale.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/noiseredu.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/noiseredu1.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/blurredimage.jpg" width="200"> |
|:--:|:--:|:--:|:--:|
| GoldenRun | NONOISE1 | NONOISE2 | BLUR |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/white.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/brightness15.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/brightness25.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/black.jpg" width="200"> |
| WHI | BRIGH1 | BRIGH2 | BLA |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/broken1-fail.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/broken1-fail2.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/nobayerfilterimage.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/sharpnesscorr.jpg" width="200"> |
| BRLE1 | BRLE2 | NBAYF | NOSHARP |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/chromabefail.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/chromabefail2.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/icebrigfail.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/icebrigfail2.jpg" width="200"> |
| NOCHROMAB-nb | NOCHROMAB-b | ICE1 | ICE2 |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/dirtyglass.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/dirtyglass2.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/rainglassfail.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/condens.jpg" width="200"> |
| DIRTY1 | DIRTY2 | RAIN | COND |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/bandingfail.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/nodemosfail.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel1.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/dead50pixel.jpg" width="200"> |
| BAND | NODEMOS | DEAPIX1 | DEAPIX50 |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/dead200pixel.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/dead1000pixel.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-1vertical-line.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-3lines-2H1V.jpg" width="200"> |
| DEAPIX200 | DEAPIX1000 | DEAPIX-vcl | DEAPIX-3l |
| <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-5lines-3H2V.jpg" width="200"> | <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-10lines-5H5V.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-carreggiata.jpg" width="200"> |  <img src="https://github.com/francescosecci/Python_Image_Failures/blob/master/failure_example/deadpixel-carregg-obstacle.jpg" width="200"> |
| DEAPIX-5l | DEAPIX-10l | DEAPIX-r | DEAPIX-ro |

<br><br>
### A detailed description of this work can be found in:

Francesco Secci, "On failures of RGB cameras and their effects in autonomous driving applications", Master Thesis at the University of Florence, Italy (in Italian only), July 2020. ([thesis](https://github.com/francescosecci/Python_Image_Failures/blob/master/Documenti/thesis.pdf))
<br><br>
Francesco Secci, Andrea Ceccarelli, "On failures of RGB cameras and their effects in autonomous driving applications", in press -- to appear at the 31st International Symposium on Software Reliability Engineering (ISSRE 2020). ([paper](https://github.com/francescosecci/Python_Image_Failures/blob/master/Documenti/Paper.pdf))

