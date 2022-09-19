#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trying to see how to integrate the Eigen localisation code with cppyy

Created on Mon Sep 19 14:43:19 2022

@author: thejasvi
"""
try:
    import cppyy
    cppyy.add_include_path('./eigen/')
    cppyy.include('./example_eigen.cpp')
    MatrixXd = cppyy.gbl.Eigen.MatrixXd
    VectorXd = cppyy.gbl.Eigen.VectorXd
except ImportError:
    MatrixXd = cppyy.gbl.Eigen.MatrixXd
    VectorXd = cppyy.gbl.Eigen.VectorXd
from companion_python_code import python_function
import numpy as np 

all_speedups = []
num_channels = []
for i in range(1000):
    
    nmics = int(np.random.choice(np.arange(4,20), 1))
    np_array = np.random.normal(1,10,3*(nmics)).reshape(-1,3)
    np_d = np.random.choice(np.linspace(-0.5,0.5,100), nmics-1)
    
    
    import time
    start = time.perf_counter_ns()
    rows, cols = np_array.shape
    
    array_geom = MatrixXd(rows, cols)
    for i in range(rows):
        for j in range(cols):
            array_geom[i,j] = np_array[i,j]
    
    d = VectorXd(rows-1)
    for i, value in enumerate(np_d):
        d[i] = value
    
    uu = cppyy.gbl.spiesberger_wahlberg_solution(array_geom, d, 343.0)
    stop = time.perf_counter_ns()
    durn_s = (stop-start)/1e9
    #print(f'%.6f seconds' % durn_s)
    # (0,6,0, 0,13,0, 1,0,0, 0,0,1, 2,2,4)
    
    start2 = time.perf_counter_ns()
    output  = python_function(np_array, np_d)
    stop2 = time.perf_counter_ns()
    durn2_s = (stop2-start2)/1e9
    
    speedup = durn2_s/durn_s
    #print(f'%.6f seconds'% durn2_s)
    #print('%.2f speed up'% speedup)
    num_channels.append(nmics)
    all_speedups.append(speedup)

import matplotlib.pyplot as plt 
print(np.percentile(all_speedups, [0,2.5,50,97.5,100]))
plt.plot(num_channels, all_speedups, '*')
