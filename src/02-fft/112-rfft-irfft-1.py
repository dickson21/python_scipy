"""
Subject : rfft, irfft
Created : 2020-08-24
Status : OK
Detail:
rfft() :  FFT of a real sequence and outputs the FFT coefficients  with separate real and imaginary parts
irfft() : IFFT of the FFT coefficients with this special ordering

Ref:
https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/fftpack.html
"""

import numpy as np 
from scipy.fftpack import fft, rfft, irfft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5, 1.0])
print(fft(x))
yr = rfft(x)
print(yr)
print(irfft(yr))
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print(fft(x))
yr = rfft(x)
print(yr)



"""
from scipy.fftpack import fft, rfft, irfft
>>> x = np.array([1.0, 2.0, 1.0, -1.0, 1.5, 1.0])
>>> fft(x)
array([ 5.5 +0.j        ,  2.25-0.4330127j , -2.75-1.29903811j,
        1.5 +0.j        , -2.75+1.29903811j,  2.25+0.4330127j ])
>>> yr = rfft(x)
>>> yr
array([ 5.5       ,  2.25      , -0.4330127 , -2.75      , -1.29903811,
        1.5       ])
>>> irfft(yr)
array([ 1. ,  2. ,  1. , -1. ,  1.5,  1. ])
>>> x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
>>> fft(x)
array([ 4.5       +0.j        ,  2.08155948-1.65109876j,
       -1.83155948+1.60822041j, -1.83155948-1.60822041j,
        2.08155948+1.65109876j])
>>> yr = rfft(x)
>>> yr
array([ 4.5       ,  2.08155948, -1.65109876, -1.83155948,  1.60822041])


[ 5.5 +0.j          2.25-0.4330127j  -2.75-1.29903811j  1.5 +0.j
 -2.75+1.29903811j  2.25+0.4330127j ]
[ 5.5         2.25       -0.4330127  -2.75       -1.29903811  1.5       ]
[ 1.   2.   1.  -1.   1.5  1. ]
[ 4.5       +0.j          2.08155948-1.65109876j -1.83155948+1.60822041j
 -1.83155948-1.60822041j  2.08155948+1.65109876j]
[ 4.5         2.08155948 -1.65109876 -1.83155948  1.60822041]
"""