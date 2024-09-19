#string:
#Def:sequence of character such as words or phrases.
#string are enclosed in quotes either single or double or triple

'''str1="Hello,good  morning"
str2='Hello,good morning'
str3="""Hello,good morning"""
print(str1)  # Hello,good  morning
print(str2)  # Hello,good  morning
print(str3)  # Hello,good  morning'''




'''s="Hello, Good Morning!"
print(s)
print("length:",len(s))

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[18])'''




'''s="Hello, Good Morning!"
print(s)   #Hello, Good Morning!


print("length:",len(s))

for i in range(len(s)) :
    print(s[i],end="")  #Hello, Good Morning!

print("\n")

print(s[0:20])   #Hello, Good Morning!


print(s[0:20:1])   #Hello, Good Morning!

print(s[19::-1])   #reverse form

'''



a=20
b=30
#addition of 20 and 30 is 50
print("Addition of",a, "and",b,'is',(a+b))
print(f"Addition of {a} and {b} is {a+b}")
print("Addition if {} and {} is {}".format(a,b,a+b))
print("Addition of %d and %d is %d" % (a,b,a+b))