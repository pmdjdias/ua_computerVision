# Aula_02_ex_03.py
#
# Historam visualization with openCV
#
# Paulo Dias 

#import
import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

####################
# Compute Histogram
####################
def compute_histogram(image,histSize, histRange):
	# Compute the histogram
	hist_item = cv2.calcHist([image], [0], None, [histSize], histRange)
	return hist_item

##########################################
# Drawing with openCV
# Create an image to display the histogram
def histogram2image(hist_item, histSize, histImageWidth, histImageHeight, color):

	histImage = np.zeros((histImageWidth, histImageHeight, 1), np.uint8)

	# Width of each histogram bar
	binWidth = int(np.ceil(histImageWidth * 1.0 / histSize))

	# Normalize values to [0, histImageHeight]
	cv2.normalize(hist_item, hist_item, 0, histImageHeight, cv2.NORM_MINMAX)

	# Draw the bars of the nomrmalized histogram
	for i in range(histSize):
		cv2.rectangle(histImage, (i * binWidth, 0), ((i + 1) * binWidth, int(hist_item[i])), color, -1)

	# ATTENTION : Y coordinate upside down
	histImage = np.flipud(histImage)

	return histImage

# Read the image from argv
#image = cv2.imread( sys.argv[1] , cv2.IMREAD_UNCHANGED );
image = cv2.imread( "../images/lena.jpg", cv2.IMREAD_UNCHANGED );
image = cv2.imread( "../images/ireland-06-02.tif", cv2.IMREAD_UNCHANGED );

if  np.shape(image) == ():
	# Failed Reading
	print("Image file could not be open!")
	exit(-1)

# Image characteristics
if len (image.shape) > 2:
	print ("The loaded image is NOT a GRAY-LEVEL image !")
	exit(-1)

# Display the image
cv2.namedWindow("Original Image")
cv2.imshow("Original Image", image)

# print some features
height, width = image.shape
nchannels = 1
print("Image Size: (%d,%d)" % (height, width))
print("Image Type: %d" % nchannels)
print("Number of elements : %d" % image.size)

print("Image Size: (%d,%d)" % (height, width))

# Size
histSize = 256	 # from 0 to 255
# Intensity Range
histRange = [0, 256]
hist_item =  compute_histogram(image,histSize, histRange)

histImageWidth = 512
histImageHeight = 512
color = (125)
histImage =  histogram2image(hist_item, histSize, histImageWidth, histImageHeight, color)

cv2.imshow('colorhist', histImage)
cv2.waitKey(0)

##########################
# Drawing using matplotlib
# plt.plot(hist_item,'r')
# plt.xlim(histRange)
# plt.show()




