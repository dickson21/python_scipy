"""
Subject : discrete cosine transform
Created : 2020-08-24
Status : OK


"""

import numpy as np 
from scipy.fftpack import dct, idct
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print(dct(dct(x, type=2, norm='ortho'), type=3, norm='ortho'))
 #[1.0, 2.0, 1.0, -1.0, 1.5]
# scaling factor 2*N = 10
print(idct(dct(x, type=2), type=2))
 # array([ 10.,  20.,  10., -10.,  15.])
# no scaling factor
print(idct(dct(x, type=2, norm='ortho'), type=2, norm='ortho'))
 #array([ 1. ,  2. ,  1. , -1. ,  1.5])
# scaling factor 2*N = 10
print(idct(dct(x, type=3), type=3))
 # array([ 10.,  20.,  10., -10.,  15.])
# no scaling factor
print(idct(dct(x, type=3, norm='ortho'), type=3, norm='ortho'))
 # array([ 1. ,  2. ,  1. , -1. ,  1.5])
# scaling factor 2*(N-1) = 8
print(idct(dct(x, type=1), type=1))
 # array([  8.,  16.,   8.,  -8.,  12.])

"""
[ 1.   2.   1.  -1.   1.5]
[ 10.  20.  10. -10.  15.]
[ 1.   2.   1.  -1.   1.5]
[ 10.  20.  10. -10.  15.]
[ 1.   2.   1.  -1.   1.5]
[ 8. 16.  8. -8. 12.]
"""