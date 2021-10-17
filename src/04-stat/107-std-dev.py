"""
std = sqrt(mean(abs(x - x.mean())**2))

If the array is [1, 2, 3, 4], then its mean is 2.5. 
Hence the squared deviations are [2.25, 0.25, 0.25, 2.25] and 
the square root of its mean divided by 4, 
i.e., 
sqrt (5/4) is 1.1180339887498949.
"""


import numpy as np 
print(np.std([1,2,3,4]))
# 1.118033988749895

