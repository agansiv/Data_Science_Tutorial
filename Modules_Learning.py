### Dealing with modules like numpy ,pandas

import numpy as np
onedim = np.array([1,2])
twodim = np.array([ [1,4],[2,3] ])
threedim =  np.array( [  [[1,2]],[[4,5]] ,[[3,4]] ])

print("onedim data ",onedim," no of dimensions :" ,onedim.ndim)
print("twodim data ",twodim," no of dimensions :" ,twodim.ndim)
print("threedim data ",threedim," no of dimensions :" ,threedim.ndim)

## get the itemsize of the array
floatdim = np.array([1,2.1])
strdim = np.array([1,"a"])
print("Itemsize of Interger is 4 bytes as shown : " ,onedim.itemsize)
print("Itemsize of Interger is 8 bytes as shown : " ,floatdim.itemsize)
print("Itemsize of Interger is 44 bytes as shown : " ,strdim.itemsize)
print(onedim.dtype) # dtype gives the datatype of the varaible
inttofloatdim = np.array([1,2],dtype=np.float64)
print(inttofloatdim.dtype)
print(inttofloatdim)
print("Size of the array :",twodim.size) #.size gives the number of elements in the array

print("shape of the array :",threedim.shape) # .shape gives the number of rows by columns
print(threedim)

print("Generate arrays")
print(np.ones((3,1,3)))
#print(np.ones((3,2)))


print("arange function ")
# Can use arange which is nothing but range in python
# For example
print(np.arange(1,5,2)) # here we are asking to start at 1 and end at 4 ( one less 5 ) and with a gap of 2


print("learning of linspace")
print(np.linspace(1,10,20)) # here we are asking to print 20 numbers with equi gap  starting from 1 to 10
print("-----------------")
print("Learning about axis")
print(twodim)
print("----------axis=0 output  adding columns-------")
print(twodim.sum(axis=0)) # axis =0 is adding up the coulmns  =0 is columns ; =1 is rows
print("-------axis =1 output adding rows ----------")
print(twodim.sum(axis=1))

