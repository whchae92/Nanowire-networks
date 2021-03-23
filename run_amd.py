# -*- coding: utf-8 -*-
"""
Created on Wed Dec 2 11:06:23 2020

@author: wchae
"""

import SEM_tools as sem
from pathlib import Path
import numpy as np

paths = Path('C:/Users/whcha/Dropbox (MIT)/Research/Data/SEM/201201_sprayAgNW/10cycles').glob('*.tif')
number_of_imgs = 11


amd_list = np.zeros(number_of_imgs) # define numpy array that stores amd values
x = 0 # initial index

for path in paths:
    img_path = str(path) # 
    amd_list[x] = sem.amd(img_path,5000, 50)
    x = x + 1 # increase index by 1 

amd_avg = np.average(amd_list)
amd_std = np.std(amd_list)