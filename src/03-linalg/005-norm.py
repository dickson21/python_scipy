

import numpy as np
from scipy import linalg
A=np.array([[1,2],[3,4]])
print(A)
print(linalg.norm(A))
linalg.norm(A,'fro') # frobenius norm is the default
linalg.norm(A,1) # L1 norm (max column sum)
linalg.norm(A,-1)
linalg.norm(A,np.inf) # L inf norm (max row sum)

"""
>>> import numpy as np
>>> from scipy import linalg
>>> A=np.array([[1,2],[3,4]])
>>> A
array([[1, 2],
      [3, 4]])
>>> linalg.norm(A)
5.4772255750516612
>>> linalg.norm(A,'fro') # frobenius norm is the default
5.4772255750516612
>>> linalg.norm(A,1) # L1 norm (max column sum)
6
>>> linalg.norm(A,-1)
4
>>> linalg.norm(A,np.inf) # L inf norm (max row sum)
7

"""