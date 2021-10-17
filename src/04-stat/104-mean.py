"""
Arithmetic mean is the sum of elements along an axis divided by the number of elements. 
The numpy.mean() function returns the arithmetic mean of elements in the array. 
If the axis is mentioned, it is calculated along it.
"""

import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 

print('Our array is:' )
print(a )


print('Applying mean() function:')
print(np.mean(a)) 


print('Applying mean() function along axis 0:') 
print(np.mean(a, axis = 0)) 

print('Applying mean() function along axis 1:' )
print(np.mean(a, axis = 1))

"""
Our array is:
[[1 2 3]
 [3 4 5]
 [4 5 6]]
Applying mean() function:
3.6666666666666665
Applying mean() function along axis 0:
[2.66666667 3.66666667 4.66666667]
Applying mean() function along axis 1:
[2. 4. 5.]
"""
