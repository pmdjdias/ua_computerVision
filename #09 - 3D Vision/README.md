# Lab 9 - 3D Vision / PointCloud processing

## Outline
* 3D point visualization from disparity images
* Visualization and manipulation of 3D cloud of points in open3D
* Registration of cloud of points using ICP in open3D
* Segmentation and Clustering

## 9.1 - Visualization of point cloud in PCL 
Modify the source code `viewcloud.py` to read the 3D points of the file you have saved in the previous section and visualize the results of the 3D reconstruction.
Assignment to the pointCloud can be performed using the following code:
```html
p = points_3D.reshape(-1, 3)
fp = []
for i in range(p.shape[0]):
    if np.all(~np.isinf(p[i)) and np.all(~np.isnan(p[i])):
        fp.append(p[i])
pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(fp)
```
Visualize the 3D points and add any filtering necessary to improve the visualization of the reconstructed 3d Points . 
Filter the point to be seen in the z axis between 0,1 and 5 either when creating the pointcloud or using the crop function as follow:
```html
# Cropping the mesh using its bouding box to remove positive Z-axis between 0.1 and 5
bbox = pcl.get_axis_aligned_bounding_box()
bbox_points = np.asarray(bbox.get_box_points())
bbox_points[:, 2] = np.clip(bbox_points[:, 2], a_min=0.1, a_max=2)
bbox_cropped = o3d.geometry.AxisAlignedBoundingBox.create_from_points(o3d.utility.Vector3dVector(bbox_points))
mesh_cropped = pcl.crop(bbox_cropped)
```
[Crop Point Cloud](http://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html#Crop-point-cloud)

You might also use the left image to add texture information to each 3D point, for these you can specify the color of the point cloud with the pcl.colors, specifying the color as an rgb value between [0,1]

##	9.2 - PCD (point cloud data) 3D format 
Modify the source code viewcloud.cpp to read and visualize the two provided kinect images `office1.pcd` and `office2.pcd` The Point Cloud Data file format (PCD) used is the 3D file format from PCL and can be written and read directly using the PCL functions `o3d.io.read_point_cloud` and `o3d.io.write_point_cloud`. 
Kinect sensor returns NaN values (when no measure was returend for a given pixel) that may cause problems in the processing. To remove NaN values you need to use the function `remove_non_finite_points`.

## Note:
You might downsample the 3D point cloud (reduce the number of points in the file) using the `voxel_down_sample` filter with a grid size of 0.05 in each direction. The `filt_office1.pcd` and `filt_office2.pcd` files have already been treated with this filter resulting in down sampled cloud of points. 
```html
pcd.remove_non_finite_points()
pcd = source.voxel_down_sample(voxel_size=0.5)
```
http://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html 


## 9.3 - ICP alignment
Use the [registration_icp](http://www.open3d.org/docs/release/tutorial/pipelines/icp_registration.html) function to align the two given cloud of points.

Note that the values of the ICP thresholds should be adapted for each case. Typically an initial rough registration should be provided to avoid bad registration. However in this case, given the proximity of the provided depth images, this should not be necessary, and the algorithm should converge to a good estimation of the transform between the two point clouds.

Visualize in the same window the original and the aligned cloud of points. Modify the ICP parameters to check the quality of the registration (for example use the default values and evaluate the results).

The evaluated transform can be recovered with the function as the `registration_icp.transformation` and you can apply the transformation to a pointcloud using the transform method.

Merge the two aligned pointclouds and save the obtain pointcloud to a new file `merged_offices.ply` (use the + operator).

## Optional
Try the previous code to align the images Lab_0.24_1.pcd and Lab_0.24_2.pcd acquired with a kinect azure sensor. Is the ICP providing a good estimation of the transform? Why?
Adapt the following code to pick at least 3 points between the two point clouds and feed the ICP algorithm with an initial transform in order to achieve a good registration.
```html
def pick_points(pcd):
    print("")
    print("1) Please pick at least three correspondences using [shift + left click]")
    print("   Press [shift + right click] to undo point picking")
    print("2) Afther picking points, press q for close the window")
    vis = o3d.visualization.VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # user picks points
    vis.destroy_window()
    print("")
    return vis.get_picked_points()

picked_id_source = pick_points(source)
picked_id_target = pick_points(target)
assert (len(picked_id_source) >= 3 and len(picked_id_target) >= 3)
assert (len(picked_id_source) == len(picked_id_target))
corr = np.zeros((len(picked_id_source), 2))
corr[:, 0] = picked_id_source
corr[:, 1] = picked_id_target
```

## 9.4 - Plane segmentation in Kinect image
Use the following code [Plane Segmentation](https://www.open3d.org/docs/release/tutorial/geometry/pointcloud.html#Plane-segmentation) to detect and crop the main plane from the previous point cloud using the segment_plane function. Modify the segment_plane value to see the results. modify the code to make it iterative to detect the 5 main planes in the scene. 
