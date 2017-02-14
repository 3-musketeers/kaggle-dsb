# from __future__ import print_function, division
import SimpleITK as sitk
import numpy as np
import csv
from glob import glob
import pandas as pd
try:
    from tqdm import tqdm # long waits are not fun
except:
    print('TQDM does make much nicer wait bars...')
    tqdm = lambda x: x

# (insert helper functions here)

# Getting list of image files
LUNA_DATA_PATH = '../../../../data/luna16/'
LUNA_SUBSET_PATH = LUNA_DATA_PATH + 'subset0/'
OUTPUT_PATH = '../../../../output/build-simple-model'
FILE_LIST = glob(LUNA_SUBSET_PATH + '*.mhd')

# Helper function to get rows in data frame associated with each file
def get_filename(file_list, case):
    for f in file_list:
        if case in f:
            return(f)
# The locations of the nodes
df_node = pd.read_csv(LUNA_DATA_PATH + "annotations.csv")
df_node["file"] = df_node["seriesuid"].map(lambda file_name: get_filename(file_list, file_name))
df_node = df_node.dropna()

# Looping over the image files
for fcount, img_file in enumerate(tqdm(FILE_LIST)): 