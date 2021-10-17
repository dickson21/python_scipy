"""
Percentile (or a centile) is a measure used in statistics 
indicating the value below which a given percentage of observations in a group of observations fall. 
The function numpy.percentile() takes the following arguments.
"""

import numpy as np 
a = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

print('Our array is:') 
print(a)  

print('Applying percentile() function:') 
print(np.percentile(a,50))  

print('Applying percentile() function along axis 1:') 
print(np.percentile(a,50, axis = 1))  

print('Applying percentile() function along axis 0:') 
print(np.percentile(a,50, axis = 0))

"""
Our array is:
[[30 40 70]
 [80 20 10]
 [50 90 60]]
Applying percentile() function:
50.0
Applying percentile() function along axis 1: row
To cover 50% of data, the value = 40 for row#0, 20 for row#1, 60 for row#2
[40. 20. 60.]
Applying percentile() function along axis 0: col
[50. 40. 60.]
"""