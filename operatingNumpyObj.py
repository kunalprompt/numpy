'''
Hello World!
http://kunalprompt.github.io

Operating NumPy Objects
'''
print __doc__

from numpy import *

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print "This a Python List of Lists - \n", lst
print "Converting this to NumPy Object..."


# creating a numpy object (ie. a multidimensional array)
num_obj = array(lst)
print num_obj
print "Type of Numpy Object - "+str(type(num_obj))
print "Number of dimensions or axes this object has are - "+str(num_obj.ndim)
print "Data Type of this object - "+str(num_obj.dtype)

x=2;y=1
print "Value of element at %d, %d of this numpy object is -"%(x, y), num_obj[x, y]

print "Type Casting this object to float"
num_obj = num_obj.astype('float')
print num_obj
# Note - NumPy Object is a homogenius multidimensional array so if only one of the element of the object is of a different type, all will be changed so.
print "Getting a subset of this object"
c = num_obj[0:2, 0:2]
print c
n=0.12
print "Adding a number %f to all the elements - "%(n)
num_obj+=n
print num_obj
print "Repeating the array elements(in succession) on row or column dimensions where "\
"row-dimension:0, and column-dimension-:1"
arr = num_obj.repeat(2, axis=0) # repeats each row twice in succession
# ndarray.repeat(<number_of_times>, <row_or_column>)
print arr
val=1.35
print "Subtracting an %f from all the elements "%(val)
arr=abs(arr-val)
print arr
print

