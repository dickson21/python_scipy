"""
Subject : discrete sine transform
Created : 2020-08-24
Status : OK
"""


import numpy as np 
from scipy.fftpack import dst, idst
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
# scaling factor 2*N = 10
idst(dst(x, type=2), type=2)
 # array([ 10.,  20.,  10., -10.,  15.])
# no scaling factor
idst(dst(x, type=2, norm='ortho'), type=2, norm='ortho')
 # array([ 1. ,  2. ,  1. , -1. ,  1.5])
# scaling factor 2*N = 10
idst(dst(x, type=3), type=3)
 # array([ 10.,  20.,  10., -10.,  15.])
# no scaling factor
idst(dst(x, type=3, norm='ortho'), type=3, norm='ortho')
 # array([ 1. ,  2. ,  1. , -1. ,  1.5])
# scaling factor 2*(N+1) = 8
idst(dst(x, type=1), type=1)
 # array([ 12.,  24.,  12., -12.,  18.])