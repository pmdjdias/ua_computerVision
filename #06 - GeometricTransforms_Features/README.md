# Lab 6 - Geometric Transformations and Feature detection 

## Outline
* Affine transformation
* Manual correspondences to evaluate affine transformation
* Keypoint detection and matching
* Homography transformation

## 6.1 - Affine transformations
Select an image of your choice and apply rotation and translation using the OpenCV transformation operations. Note that you can easily combine scaling and rotation when defining the transformation matrix.
You can create the rotation matrix using the following code:
```html
rows,cols,channels  = src.shape
M = cv2.getRotationMatrix2D((0,0),25,1)
print(M)
M[0][2] = -50
M[1][2] = 100
print(M) 
```
Save the image transformed after applying the function `warpAffine` with the name `imagename_tf.jpg`.

Check the website from OpenCV to see other examples of possible transform:

https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html

## 6.2 - Evaluation of transformation using manual selection
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

Print the estimated matrix and compute the different transformation parameters from the matrix to check if the transform was correctly evaluated. 
You may use the following formulas (import the math package) to compute the transformation parameters:

Considering that

$`
\begin{bmatrix}
\begin{array}{cc} 
a & b & tx\\
b & d & ty
\end{array}
\end{bmatrix} = 
\quad
\begin{bmatrix}
\begin{array}{cc} 
s_x cos\psi & -s_xsin\psi & x_c\\
s_ysin\psi & s_ycos\psi & y_c
\end{array}
\end{bmatrix} 
`$

Then 

$`
\begin{split}
t_x = x_c\\
t_y = y_c
\end{split}
`$

$`
\begin{split}
s_x=sign(a)\sqrt{a^2+b^2}\\
s_y=sign(d)\sqrt{c^2+d^2}\\
\end{split}
`$

and
$`
tan(\psi) = -\frac{b}{a} = \frac{c}{d}
`$
 
You may also show the result of subtracting images after warping to evaluate the correctness of the evaluated transform.

## 6.3 - Find keypoints in both Images using the SIFT algorithm 
Use SIFT (Scale-Invariant Feature Transform) to detect points of interest in the original and transformed image.
You may use the following code:
```html
# Initiate SIFT detector
sift = cv2.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(src,None)
```

Display the detected points in each of the images using the drawKeypoints functions.

More information in:

https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

[comment]: <> (Aqui talvez melhor usar exemplo do brute force e depois passar para o FLAN como optional(/Extra))
## 6.4 - Find correspondences between keypoints using Brute Force matcher
Use a Brute Force matcher to find corresponding points between the two images.
https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html
```html
# create BFMatcher object
bf = cv2.BFMatcher(cv2.DescriptorMatcher_BRUTEFORCE, crossCheck=True)
# Match descriptors.
matches = bf.match(des1,des2)
# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Remove not so good matches
numGoodMatches = int(len(matches) * 0.1)
matches = matches[:numGoodMatches]


# Draw matches
im_matches = cv2.drawMatches(src,kp1,dst,kp2,matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv2.imshow("matches",im_matches)

# Evaluate transform
src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
```
Modify the number of matches to consider and see its impact.

## 6.5 - Evaluation of transformation with automatic selection
Use the correspondences from the brute matcher to evaluate again the transform between the two images as in question 6.2. Do not forget the conversion numpy array.
```html
# Conversion to np array
src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ]).reshape(-1,1,2)
```

Optional: you may use other strategies (for example the FLANN based Matcher) to find correspondences between the images.

https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html


## 6.6 - Homography estimation 	
Consider the images `homography_1.jpg` to `homography_4.jpg`. 
These are images taken from a book from different viewpoints such that the image is suffering an homography transform.
Adapt the code of the previous exercises to select manually the corners of the book in the image and evaluate/correct the homography.
Use the `findHomography` and `warpPerspective` function from OpenCV.
Consider that the book is 17.5 x 23.5 cm.

https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html
