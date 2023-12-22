 # viewcloud.py
 #
 # open3D examepl to view a point cloud
 #
 # Paulo Dias

import numpy as np
import open3d as o3d

# Create array of random points between [-1,1]
pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(np.random.rand(2500,3) * 2 - 1)
#pcl.paint_uniform_color([0.0, 0.0, 0.0])

# Create axes mesh
Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(1)

# shome meshes in view
o3d.visualization.draw_geometries([pcl , Axes])



