"""
Subject : 2D, N-dim fft
Status : OK
Detail:
The functions fft2 and ifft2 provide 2-dimensional FFT, and IFFT, respectively
fftn and ifftn provide n-dimensional FFT, and IFFT, respectively.
The example below demonstrates a 2-dimensional IFFT and plots the resulting (2-dimensional) time-domain signals

Ref:
https://docs.scipy.org/doc/scipy-1.3.1/reference/tutorial/fftpack.html
"""

import numpy as np 
from scipy.fftpack import ifftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N))
xf[0, 5] = 1
xf[0, N-5] = 1
Z = ifftn(xf)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 0] = 1
xf[N-5, 0] = 1
Z = ifftn(xf)
ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 10] = 1
xf[N-5, N-10] = 1
Z = ifftn(xf)
ax3.imshow(xf, cmap=cm.Reds)
ax6.imshow(np.real(Z), cmap=cm.gray)
plt.show()