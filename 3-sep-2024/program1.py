from array import *
arr=array("i",[12,43,87,46])
#if we enter alphabet shows error
#arr=array("i",[12,43,87,46])
print(type(arr))
print(arr)
print(arr.typecode)
print(arr.tolist())

#replace
arr[arr.index(87)]=40
print(arr.tolist())
#or
arr[2]=40
print(arr.tolist())

#append add any no.
arr.append(100)
print(arr.tolist())

#insert any number in array
arr.insert(2,50)
arr.insert(len(arr),99)   #to add number at last of array
print(arr.tolist())

#to add list of elements  in array (extend)
arr.extend([88,85,87])
print(arr.tolist())

#add tuple in array
arr.extend({1,2,3})
print(arr.tolist())


#remove any  element from array
arr.remove(88)
print(arr.tolist())

#remove item using index
arr.pop(2)
print(arr.tolist())

#how many time item came
print("occurance (100):",arr.count(100))

#slicing to print no. from upto 1----6
print("array:",arr)
print("slicing of array:",arr[0:5])
print("slicing of array:",arr[0:len(arr)])
print("slicing of array:",arr[0:8:2])
print("reverse of array:",arr[len(arr)::-1])






