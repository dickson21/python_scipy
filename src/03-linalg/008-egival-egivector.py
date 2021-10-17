

import numpy as np
from scipy import linalg
A = np.array([[1, 2], [3, 4]])
la, v = linalg.eig(A)
l1, l2 = la
print(l1, l2)   # eigenvalues
# (-0.3722813232690143+0j) (5.372281323269014+0j)
print(v[:, 0])   # first eigenvector
# [-0.82456484  0.56576746]
print(v[:, 1])   # second eigenvector
# [-0.41597356 -0.90937671]
print(np.sum(abs(v**2), axis=0))  # eigenvectors are unitary
# [1. 1.]
v1 = np.array(v[:, 0]).T
print(linalg.norm(A.dot(v1) - l1*v1))  # check the computation
# 3.23682852457e-16

"""
>>> import numpy as np
>>> from scipy import linalg
>>> A = np.array([[1, 2], [3, 4]])
>>> la, v = linalg.eig(A)
>>> l1, l2 = la
>>> print(l1, l2)   # eigenvalues
(-0.3722813232690143+0j) (5.372281323269014+0j)
>>> print(v[:, 0])   # first eigenvector
[-0.82456484  0.56576746]
>>> print(v[:, 1])   # second eigenvector
[-0.41597356 -0.90937671]
>>> print(np.sum(abs(v**2), axis=0))  # eigenvectors are unitary
[1. 1.]
>>> v1 = np.array(v[:, 0]).T
>>> print(linalg.norm(A.dot(v1) - l1*v1))  # check the computation
3.23682852457e-16

"""