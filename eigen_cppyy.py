# -*- coding: utf-8 -*-
"""
Trying out cppyy with Eigen 

Created on Fri Sep 16 12:46:25 2022

@author: theja
"""

import cppyy
import numpy as np
cppyy.add_include_path('./eigen/')





if __name__ == '__main__':
    array_geom = np.array([[0,0,0],
                           [0,1,0],
                           [1,0,0],
                           [0,0,1],
                           ])
    print(np.linalg.pinv(array_geom[1:,:]))