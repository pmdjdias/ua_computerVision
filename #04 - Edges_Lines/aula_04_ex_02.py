# Aula_04_ex_02.py
#
# Mean Filter
#
# Paulo Dias 

#import
import sys
import numpy as np
import cv2

def printImageFeatures(image):
	# Image characteristics
	if len(image.shape) == 2:
		height, width = image.shape
		nchannels = 1
	else:
		height, width, nchannels = image.shape

	# print some features
	print("Image Height: %d" % height)
	print("Image Width: %d" % width)
	print("Image channels: %d" % nchannels)
	print("Number of elements : %d" % image.size)

# Read the image from argv
#image = cv2.imread( sys.argv[1] , cv2.IMREAD_GRAYSCALE );
image = cv2.imread( "./lena.jpg", cv2.IMREAD_GRAYSCALE );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

printImageFeatures(image)

cv2.imshow('Orginal', image)

# Average filter 3 x 3
imageAFilter3x3_1 = cv2.blur( image, (3, 3))
cv2.namedWindow( "Average Filter 3 x 3 - 1 Iter", cv2.WINDOW_AUTOSIZE )
cv2.imshow( "Average Filter 3 x 3 - 1 Iter", imageAFilter3x3_1 )

cv2.waitKey(0)


