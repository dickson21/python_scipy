"""
Detail :
 AX   = b
 AA'X = A'b
   X  = A'b

 A' = inverse of A  

"""

import numpy as np
from scipy import linalg
A = np.array([[1, 2], [3, 4]])
print(A)
b = np.array([[5], [6]])
print(b)
linalg.inv(A).dot(b)  # slow
A.dot(linalg.inv(A).dot(b)) - b  # check
print(np.linalg.solve(A, b))  # fast
A.dot(np.linalg.solve(A, b)) - b  # check


"""
>>> import numpy as np
>>> from scipy import linalg
>>> A = np.array([[1, 2], [3, 4]])
>>> A
array([[1, 2],
      [3, 4]])
>>> b = np.array([[5], [6]])
>>> b
array([[5],
      [6]])
>>> linalg.inv(A).dot(b)  # slow
array([[-4. ],
      [ 4.5]])
>>> A.dot(linalg.inv(A).dot(b)) - b  # check
array([[  8.88178420e-16],
      [  2.66453526e-15]])
>>> np.linalg.solve(A, b)  # fast
array([[-4. ],
      [ 4.5]])
>>> A.dot(np.linalg.solve(A, b)) - b  # check
array([[ 0.],
      [ 0.]])
"""      