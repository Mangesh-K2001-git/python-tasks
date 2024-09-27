

# -------------------------------------------------------------------------------------------


# Set comprehension:
# syntax:
# {Expression for variable in iterable if condition}

# #Ex1.we have set of list of number amd get set of even numbers from it
# a = [1,2,3,2,4,6,8,6,9,3,2,1,3,5,4]
# even = [x for x in a if x%2==0]
# print(even)

# -----------------------------------------------------------------------------------
# Dict comprehension:
# syntax:
# {key :values for variables for iterable if condition}

# Ex1.we have list of number and get dict of square of numbers from it
# a = [1,2,3,4,]
# square = {x: x**2 for x in a}
# print(square)

# #Ex2.dict of {city:temp}->{city:temp}
# a = {"delhi":30,"mumbai":35,"chennai":40,"bangal":38}
# t = {city:temp*(9/5)+32 for city,temp in a.items()}
# print(t)


# #Ex3.make a dictionary of factorial from given list
# a = [1,2,3,4,5,6,]
# import math
# f = {x:math.factorial(x) for x in a}
# print(f)


#Ex4.
a=["a","b","c"]
b=["Airpods","Batman","Captain"]

d={a[i]:b[i] for i in range(len(a))}
print(d)

s={key:value for key,value in zip(a,b)}
print(s)
