#select
import numpy as np 


x = np.arange(10)
condlist = [x<3, x>5]
choicelist = [x, x**2]
result = np.select(condlist, choicelist)
print(result)

"""
array([ 0,  1,  2,  0,  0,  0, 36, 49, 64, 81])
"""
