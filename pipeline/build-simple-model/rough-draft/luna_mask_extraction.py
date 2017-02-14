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