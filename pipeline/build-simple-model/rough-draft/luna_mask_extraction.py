import SimpleITK as sitk
import numpy as np
import csv
from glob import glob
import pandas as pd

# path constants
LUNA_DATA_PATH = '../../../../data/luna16/'
LUNA_SUBSET_PATH = LUNA_DATA_PATH + 'subset0/'

file_list = glob(LUNA_SUBSET_PATH + "*.mhd") # get all the mhd image files

# Helper function to get rows in data frame associated with each file
def get_filename(case):
    global file_list
    for f in file_list: # for every file in the list if the seriesuid is in the file name, return the file 
        if case in f:
            return(f)

# The locations of the nodes
df_node = pd.read_csv(LUNA_DATA_PATH + "annotations.csv")
df_node["file"] = df_node["seriesuid"].apply(get_filename) # for every rowsave file name to the 'file' column of the row
df_node = df_node.dropna() # if the seriesuid is not found in this subset, drop all the rows that have na as values for 'file' column

# Looping over the image files
fcount = 0
for img_file in file_list:
    print "Getting mask for image file %s" % img_file.replace(LUNA_SUBSET_PATH,"") # state the image file name (without path)
    mini_df = df_node[df_node["file"]==img_file] # get all nodules associate with file
    if len(mini_df)>0:       # some files may not have a nodule--skipping those 
        biggest_node = np.argsort(mini_df["diameter_mm"].values)[-1]   # just using the biggest node
        node_x = mini_df["coordX"].values[biggest_node]
        node_y = mini_df["coordY"].values[biggest_node]
        node_z = mini_df["coordZ"].values[biggest_node]
        diam = mini_df["diameter_mm"].values[biggest_node]
        
        itk_img = sitk.ReadImage(img_file) 
        img_array = sitk.GetArrayFromImage(itk_img) # indexes are z,y,x (notice the ordering)
        center = np.array([node_x,node_y,node_z])   # nodule center
        origin = np.array(itk_img.GetOrigin())      # x,y,z  Origin in world coordinates (mm)
        spacing = np.array(itk_img.GetSpacing())    # spacing of voxels in world coor. (mm)
        v_center =np.rint((center-origin)/spacing)  # nodule center in voxel space (still x,y,z ordering)
        
        def make_mask(center,diam,z,width,height,spacing,origin):
        ...
        for v_x in v_xrange:
            for v_y in v_yrange:
                p_x = spacing[0]*v_x + origin[0]
                p_y = spacing[1]*v_y + origin[1]
                if np.linalg.norm(center-np.array([p_x,p_y,z]))<=diam:
                    mask[int((p_y-origin[1])/spacing[1]),int((p_x-origin[0])/spacing[0])] = 1.0
        return(mask)
        
        i = 0
        for i_z in range(int(v_center[2])-1,int(v_center[2])+2):
            mask = make_mask(center,diam,i_z*spacing[2]+origin[2],width,height,spacing,origin)
            masks[i] = mask
            imgs[i] = matrix2int16(img_array[i_z])
            i+=1
        np.save(output_path+"images_%d.npy" % (fcount) ,imgs)
        np.save(output_path+"masks_%d.npy" % (fcount) ,masks)
