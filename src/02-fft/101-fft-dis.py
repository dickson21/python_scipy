
#basic fft
#status : OK

"""
Ref:
Python Error: ImportError: No module named FFT
https://stackoverflow.com/questions/23781095/python-error-importerror-no-module-named-fft

"""

import numpy as np 
#from scipy.fft import fft, ifft
#from numpy import fft
from numpy.fft import *

t = np.array([1,2,3,4,5])
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
print(y)
#plt.plot(t,y)
"""
[ 4.5       +0.j          2.08155948-1.65109876j -1.83155948+1.60822041j
 -1.83155948-1.60822041j  2.08155948+1.65109876j]

even N=0, N=2 : contains +ve freq term eg.N=2 +1.608j
odd  N=1, N=3 : contains -ve freq term eg N=1 -1.608j
"""
yinv = ifft(y)
print(yinv)
#array([ 1.0+0.j,  2.0+0.j,  1.0+0.j, -1.0+0.j,  1.5+0.j])

"""
from scipy.fft import fft, ifft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
yinv
array([ 4.5       +0.j        ,  2.08155948-1.65109876j,
       -1.83155948+1.60822041j, -1.83155948-1.60822041j,
        2.08155948+1.65109876j])
yinv = ifft(y)
yinv
array([ 1.0+0.j,  2.0+0.j,  1.0+0.j, -1.0+0.j,  1.5+0.j])
"""