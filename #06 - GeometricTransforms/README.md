# Lab 6 - Geometric Transformations and Feature detection 

## Outline
* Affine transformation
* Manual correspondences to evaluate affine transformation
* Keypoint detection and matching
* Homography evaluation

##	Affine transformations
Select an image of your choice and apply rotation and translation using the OpenCV transformation operations. Note that you can easily combine scaling and rotation when defining the transformation matrix.
You can create the rotation matrix using the following code:
```html
rows,cols,channels  = src.shape
M = cv2.getRotationMatrix2D((0,0),25,1)
print(M)
M[0][2] = -50
M[1][2] = 100
print(M) print(M) 
```
Save the image with the name `imagename_tf.jpg`
Check the website from OpenCV and try some transform. See some of the matrix:
https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html

##	Evaluation of transformation using manual selection
Open the original image and the transformed image. Use the following code (replicated for each images) to select 3 corresponding points in each image in the same order.
```html
def select_src(event, x, y, flags, params):
    global  srcPts
    if event == cv2.EVENT_LBUTTONDOWN:
        srcPts.append((x,y))
        cv2.circle(src, (x, y), 2, (255, 0, 0), 2)
        cv2.putText(src,str(len(srcPts)), (x+10,y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
        cv2.imshow("orginal", src)
```
After the selection, use the function `getAffineTransform` to estimate the transformation between the two images. Notice that this function only accepts 3 points as entry.
You need to convert the points to feed the getAffineTransform function:
```html
np_srcPts = np.array(srcPts).astype(np.float32)
```

Warp and display the transformed image using the warpAffine  function using a code similar to:
```html
warp_dst = cv2.warpAffine(src, transformation_rigid_matrix, (src.shape[1], src.shape[0]))
```

Print the estimated matrix and compute the different transformation parameters from the matrix to check if the matrix was correctly evaluated. You may use the following formulas and import the math package to compute mathematical computations:
```
Wirte the equations here, missing!
``
 
You may subtract both images after warping to evaluate the correctness of the evaluated transform.

##	Find keypoints in both Images using the SIFT algorithm 
Detect points of interest in both image using the SIFT (Scale-Invariant Feature Transform).
You may use the following code:
```html
# Initiate SIFT detector
sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(src,None)
```

Display the detected points in each of the images.

More information in:
https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

[comment]: <> (Aqui talvez melhor usar exemplo do brute force e depois passar para o FLAN como optional(/Extra))
##	Find correspondences between keypoints using FLAN based matcher
Use a FLAN matcher to find corresponding points between the two images.
https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html 
```html
MIN_MATCH_COUNT = 10
DISTANCE_RATIO = 0.95
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < DISTANCE_RATIO*n.distance: # Equivalente a ratio abaixo do DISTANCE_RATIO : m.distance/n.distance < DISTANCE_RATIO
        good.append(m)
        
#draw correspondences
draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = None, # draw only inliers
                   flags = 2)
        
if len(good)>MIN_MATCH_COUNT:
    img3 = cv2.drawMatches(src,kp1,dst,kp2,good,None,**draw_params)
    cv2.imshow('gray',img3)
else:
    print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )

cv2.waitKey(-1)
```
Modify some parameters of the matcher: min_match count, search parameters and threshold to evaluate the impact of these parameters on the matching.

Optional: you can use other strategy for the matching such as Brute Force Matcher
https://docs.opencv.org/4.8.0/dc/dc3/tutorial_py_matcher.html.

##	Evaluation of transformation with automatic selection
Use the correspondences from the flann matcher to evaluate again the transform between the two images as in question 6.2.


##	Homography estimation 	
Consider the images `homography_1` to `homography_4.jpg`. These are images taken from a book from different position and thus the book is suffering an homography transform.
Use previous code to select the corners of the book in the image evaluate and correct the homography using the `findHomography` and `warpPerspective` function from OpenCV.
Consider that the book is 17.5 x 23.5 cm.
https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html
