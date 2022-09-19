#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Companion code to test Cpp code
================================
Created on Fri Sep 16 13:40:57 2022

@author: thejasvi
"""
import numpy as np 
import time 
matmul = np.matmul

def python_function(array_geom, d, c=343.0):
    tau = d/c
    R = array_geom[1:,:]
    R_inv = np.linalg.pinv(R)

        
    Nrec_minus1 = R.shape[0]
    b = np.zeros(Nrec_minus1)
    f = np.zeros(Nrec_minus1)
    g = np.zeros(Nrec_minus1)
    #print(R, tau)
    for i in range(Nrec_minus1):
        b[i] = np.linalg.norm(R[i,:])**2 - (c*tau[i])**2
        f[i] = (c**2)*tau[i]
        g[i] = 0.5*(c**2-c**2)

    a1 = matmul(matmul(R_inv, b).T, matmul(R_inv,b))
    a2 = matmul(matmul(R_inv, b).T, matmul(R_inv,f))
    a3 = matmul(matmul(R_inv, f).T, matmul(R_inv,f))

    a_quad = a3 - c**2
    b_quad = -a2
    c_quad = a1/4.0

    t_soln1 = (-b_quad + np.sqrt(b_quad**2 - 4*a_quad*c_quad))/(2*a_quad)
    t_soln2 = (-b_quad - np.sqrt(b_quad**2 - 4*a_quad*c_quad))/(2*a_quad)

    s1 = matmul(R_inv,b*0.5) - matmul(R_inv,f)*t_soln1
    s2 = matmul(R_inv,b*0.5) - matmul(R_inv,f)*t_soln2
    return [s1,s2]
if __name__ == '__main__':
    
    
    start = time.perf_counter_ns()
    c = 343.0
    array_geom = np.array([0,6,0, 0,13,0, 1,0,0, 0,0,1, 2,2,4 ]).reshape(-1,3)
    d = np.array([0.01, 0.2, -0.3, 0.5])
    tau = d/c
    R = array_geom[1:,:]
    R_inv = np.linalg.pinv(R)
    stop = time.perf_counter_ns()
    
        
    Nrec_minus1 = R.shape[0]
    b = np.zeros(Nrec_minus1)
    f = np.zeros(Nrec_minus1)
    g = np.zeros(Nrec_minus1)
    #print(R, tau)
    for i in range(Nrec_minus1):
        b[i] = np.linalg.norm(R[i,:])**2 - (c*tau[i])**2
        f[i] = (c**2)*tau[i]
        g[i] = 0.5*(c**2-c**2)
    
    a1 = matmul(matmul(R_inv, b).T, matmul(R_inv,b))
    a2 = matmul(matmul(R_inv, b).T, matmul(R_inv,f))
    a3 = matmul(matmul(R_inv, f).T, matmul(R_inv,f))
    
    a_quad = a3 - c**2
    b_quad = -a2
    c_quad = a1/4.0
    
    t_soln1 = (-b_quad + np.sqrt(b_quad**2 - 4*a_quad*c_quad))/(2*a_quad)
    t_soln2 = (-b_quad - np.sqrt(b_quad**2 - 4*a_quad*c_quad))/(2*a_quad)
    
    s1 = matmul(R_inv,b*0.5) - matmul(R_inv,f)*t_soln1
    s2 = matmul(R_inv,b*0.5) - matmul(R_inv,f)*t_soln2
    
    print(f'{(stop-start)} ns elapsed')
    
