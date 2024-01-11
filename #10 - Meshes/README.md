# Lab 10 - 3D Vision / Mesh processing

## Outline
* Normal estimation
* Poisson surface reconstruction
* Mesh properties
* Mesh operations


## 10.1 - Normal Estimation
Analyze the code in file `Aula_10_01_Mesh.py` showing some basics operations on meshes.
Add the following code to acess the vertexes of the model and show the computed normals.
```html
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.asarray(mesh.vertices))
pcd.estimate_normals()
o3d.visualization.draw_geometries([pcd],point_show_normal=True )
```

## 10.2 - Surface Reconstruction
Read the `merged_office.ply` from last lecture and compute and visualize the normals for the point cloud. 
This step is important since many surface reconstruction algorithm require normal estimation to compute a 3D mesh from a pointCloud.
Add an axes frame to the windows to help understand the coordinate system.
```html
mesh_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1, origin=[0, 0, 0])
o3d.visualization.draw_geometries([downpcd, mesh_frame],point_show_normal=True )
```

Now apply the Poisson surface reconstruction algorithm, and see the result.
You should notice that normals are pointing towards the camera, this is why triangles are only shown in the back of the moodle (due to back face culling). You can deactivate back face culling with the option `mesh_show_back_face=True` in the drawgeometries or you can orient the normals in a given direction using the following code (in this case towards the negative z axis). See the results, what is the difference?
```html
downpcd.orient_normals_to_align_with_direction([0,0,-1])
```
Save the triangle mesh obtained with the name `mesh_offices.ply`.
##Optional
You may test other surface reconstruction algorithms [Alpha shapes and ball pivoting](http://www.open3d.org/docs/release/tutorial/geometry/surface_reconstruction.html#)

## 10.3 - Mesh Properties
Analyze the code `Meshproperties.py` to evaluate [mesh properties](http://www.open3d.org/docs/release/tutorial/geometry/mesh.html#Mesh-properties). See the tutorial to understand the different mesh properties. 

## 10.4 - Mesh operations
Apply some of the following operations to the mesh `mesh_offices-ply` changing the parameters to understand what the operations are performing:
* [Sampling](http://www.open3d.org/docs/release/tutorial/geometry/mesh.html#Sampling)
* [Subdivision](http://www.open3d.org/docs/release/tutorial/geometry/mesh.html#Mesh-subdivision )
* [Simplification / vertex clustering](http://www.open3d.org/docs/release/tutorial/geometry/mesh.html#Vertex-clustering)
* [Simplification / Decimation](http://www.open3d.org/docs/release/tutorial/geometry/mesh.html#Mesh-decimation)

Run the `check_properties` function on a smallest decimated version of the mesh and see if the properties are according to what you expect.
