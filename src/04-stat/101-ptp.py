"""
numpy.ptp() :
the range (maximum-minimum) of values along an axis
"""

import numpy as np 
a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 

print('Our array is:') 
print(a )
#print('\n') 

print('Applying ptp() function:') 
print(np.ptp(a) ) #max range of matrix
#print('\n') 

print('Applying ptp() function along axis 1:') 
print(np.ptp(a, axis = 1)) #1:row
#print('\n')   

print('Applying ptp() function along axis 0:')
print(np.ptp(a, axis = 0) ) #0:col

"""
Our array is:
[[3 7 5]
 [8 4 3]
 [2 4 9]]

Applying ptp() function:
7

Applying ptp() function along axis 1:
[4 5 7]

Applying ptp() function along axis 0:
[6 3 6]
"""