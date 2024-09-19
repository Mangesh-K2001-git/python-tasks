#list in python:
#list are collection of items that can any data type
#list denoted by square[]

#-----------------------------------------------------------
#EX1.
nums=[2,4,6,8,9,0]
print(type(nums))
#output:<class 'list'>

#EX2.
mylist=[23,54,5,True,"Mangesh"]
print(mylist)

#EX3.
# 0 1 2 3 4  +ve indexing
a=[33 ,55 ,77 ,99 ,88]
# -5,-4,-3,-2,-1 -ve indexing
print("list:",a)
print(a[1])
print(a[-3])



#EX4.
b=[33,11,43,21,99]
print("list:",b)
print("sorted list:",b.sort())
print("list:",b)
print("sorted list:",b.sort(reverse=True))
print("list:",b)


#EX5.removal of element
Mylist=[2,4,3,6,8]
print("original list:",Mylist)
Mylist[2]=8
print("list after modify:",Mylist)
Mylist.remove(6)
Mylist.remove(4)


#EX6.add new element
mylist=[2,4,3,6,8]
print("original list:",mylist)
#append:to insert no. in last
mylist.append(9)
print("list after append:",mylist)
#insert:to insert no.in middle
mylist.insert(7,1)
print("list after insert:",mylist)

#EX7.to find index(position)in index
mylist=[2,4,5,6,7,8,5,3,7,9]
print("index of 8:",mylist.index(8))

#EX8.to find min max
mylist=[2,4,3,5,7,6]
print("max element:",max(mylist))
print("min element:",min(mylist))
print("sum  element:",sum(mylist))


#EX9.reserve list
mylist=[1,2,3,4,5,6]
print("original list:",mylist)
mylist.reverse()
print("list after reverse:",mylist)
mylist=[2,3,4,4,5]
print("original list:",mylist)
mylist.insert(1,9)
print("list after inserting:",mylist)

 
