

import numpy as np
from scipy import linalg
A = np.array([[1,2],[3,4]])
print(A)
"""
array([[1, 2],
      [3, 4]])
"""
print(linalg.det(A))
# -2.0