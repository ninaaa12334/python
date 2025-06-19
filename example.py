import numpy as np


#create a 2D Array
arr_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr_2d)

element=arr_2d[1,2]
print(element)

dimensions=arr_2d.ndim
print(dimensions)

#seperate this array
sub_array=arr_2d[:2,:2]
print(sub_array)

sub_array2=arr_2d[-4:,-4]
print(sub_array2)

sum=np.sum(arr_2d)
print(sum)

mesatarja=np

