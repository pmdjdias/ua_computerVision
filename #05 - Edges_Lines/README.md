# Lab 5 - Filtering, edge detection

## Outline
* Thresholding
* Filters: filtering and noise attenuation / removal
* The Sobel operator: computing the image gradient
* The Canny detector: contour segmentation

[OpenCV Filtering operations](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html) 

## 5.1 - Thresholding 
Create a new program (`aula_05_exe_01.py`) that allows applying Thresholding operations to gray-level images. Use the corresponding OpenCV function and create a resulting image for each one of the possible operation types: THRESH_BINARY, THRESH_BINARY_INV, THRESH_TRUNC, THRESH_TOZERO and THRESH_TOZERO_INV.

## 5.2 - Averaging Filters
Compile and test the file `aula_05_exe_02.py`. 
Analyze the code and verify how an averaging filter is applied using the function:
``` html
dst = cv2.blur(src, ksize[, dst[, anchor[, borderType]]])
```
Write additional code allowing to:
*	Apply (5 × 5) and (7 × 7) averaging filters to a given image.
*	Apply successively (e.g., 3 times) the same filter to the resulting image.
*	Visualize and compare the results of the successive operations.
Test the developed operations using the `Lena_Ruido.png` and `DETI_Ruido.png` images.
Use the code of the previous example to analyze the effects of applying different **averaging filters** to various images, and to compare the resulting images among themselves and with the original image.
Use the following test images: `fce5noi3.bmp`, `fce5noi4.bmp`, `fce5noi6.bmp`, `sta2.bmp`, `sta2noi1.bmp`.

## 5.3 - Median Filters
Create a new example (`aula_05_exe_03.py`) that allows, similarly to the previous example, applying median filters to a given image.
Use the function:
``` html
dst = cv2.medianBlur(src, ksize[, dst])
```

Test the developed operations using the `Lena_Ruido.png` and `DETI_Ruido.png` images.
Use the developed code to analyze the effects of applying different **median filters** to various images, and to compare the resulting images among themselves and with the original image, as well as with the results of applying **averaging filters**.
Use the same test images as before.

## 5.4 - Gaussian Filters
Create a new example (`aula_05_exe_04.py`) that allows, similarly to the previous example, applying Gaussian filters to a given image.
Use the function:
``` html
Dst = cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])
```

Test the developed operations using the `Lena_Ruido.png` and `DETI_Ruido.png` images.
Use the developed code to analyze the effects of applying different **Gaussian filters** to various images, and to compare the resulting images among themselves and with the original image, as well as with the results of applying **averaging filters** and **median filters**.
Use the same test images as before.

## 5.5 - Canny detector
Create a new example (`aula_05_exe_05.py`) that allows applyies the Canny detector to a given image.
Use the function:
``` html
edges = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]])
```

Note that this detector uses hysteresis and needs two threshold values: the larger value (e.g., 100) to determine “stronger” contours; the smaller value (e.g., 75) to allow identifying other contours connected to a “stronger” one.
Test the developed operations using the `wdg2.bmp`, `lena.jpg`, `cln1.bmp` and `Bikesgray.jpg` images.

Use different threshold values: for instance, 1 and 255; 220 and 225; 1 and 128.

## Optional
Perform this operation not on a static image but using the feed of the camera
```html
import cv2
capture = cv2.VideoCapture(0)
while (True):
    ret, frame = capture.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
```

## 5.6 - Hough Line detection 
Implement a program to detect lines on an image of your choice. Adjust the parameters to get the best Canny edges as possible and then use the Hough Line transform to detect lines in the image.
[Tutorial Hough Lines](https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html)
