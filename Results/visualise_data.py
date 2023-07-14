import os
import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt

#---------------------------
#inputs
#---------------------------
var2plot="p" #p=pressure [Pa], cfx=x-skin-friction, cfy=y-skin-friction, cfz=z-skin-friction, T=temperature [K], q=heat flux [W/m^2)
var_max=4500
var_min=0
#---------------------------

#dynamic pressures from boundary conditions
rhos=np.array([0.005])
vs=np.array([1689.7])
pdyns=0.5*rhos*vs**2

#path to .npy files
path= os.getcwd() + "\\" 
#get data to read in 
X=np.load(path + 'X_data.npy')
Y=np.load(path + 'Y_data.npy')
Z=np.load(path + 'Z_data.npy')
p=np.load(path + 'p_data.npy')
cfx=np.load(path + 'cfx_data.npy')
cfy=np.load(path + 'cfy_data.npy')
cfz=np.load(path + 'cfz_data.npy')
T=np.load(path + 'T_data.npy')
#heat flux data not provided for adia (0 heat flux)
q=np.load(path + 'q_data.npy')

#normalise for the colormap
var_norm = (eval(var2plot) - var_min) / (var_max - var_min)
#import and modify the colormap from matplotlib
cmap=plt.get_cmap("jet")
cols=cmap(var_norm)[:,0:3]

#visualise 3d contours
xyz=np.transpose(np.vstack((np.vstack((X,Y)),Z)))
pcd = o3d.geometry.PointCloud()
#set up xyz pointcloud
pcd.points = o3d.utility.Vector3dVector(xyz)
#set up 3d array for point coloring (according to variable max pointcloud
pcd.colors = o3d.utility.Vector3dVector(cols)
#write pointcloud file
o3d.io.write_point_cloud("sync.ply", pcd)
pcd_load = o3d.io.read_point_cloud("sync.ply")
#visualise data
o3d.visualization.draw_geometries([pcd_load])





