


import numpy as np
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(A)
print(linalg.inv(A))
print(A.dot(linalg.inv(A))) #double check

"""
>>> import numpy as np
>>> from scipy import linalg
>>> A = np.array([[1,3,5],[2,5,1],[2,3,8]])
>>> A
array([[1, 3, 5],
      [2, 5, 1],
      [2, 3, 8]])
>>> linalg.inv(A)
array([[-1.48,  0.36,  0.88],
      [ 0.56,  0.08, -0.36],
      [ 0.16, -0.12,  0.04]])
>>> A.dot(linalg.inv(A)) #double check
array([[  1.00000000e+00,  -1.11022302e-16,  -5.55111512e-17],
      [  3.05311332e-16,   1.00000000e+00,   1.87350135e-16],
      [  2.22044605e-16,  -1.11022302e-16,   1.00000000e+00]])
"""