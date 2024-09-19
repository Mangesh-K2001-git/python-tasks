#EX1.
str1="hello good morning"
str2='''hello good morning'''
str3='hello good morning'
print(str1)
print(str2)
print(str3)


#EX2.Escape sequence character: \",\',\n,\t

str1="Hello,good morning!"

d1='Ramesh said,"I want apple"'
print(d1)
d2="Ramesh said,\"I want apple\"."
print(d2)
d3 ="Ramesh say's\"I want apple\"."
print(d3)
d4='Ramesh say\'s,"I want apple"'
print(d4)
d5='Ramesh say\'s,"Hello Ji\nkese ho".'
print(d5)
d6='Ramesh'



#EX3.string concatenation
str1="hello,"
str2="good morning!"
str3=str1+" "+str2
print(str3)



#EX4.formated string
#F string is feature in python that allows you to embed
#but f prefix before string

a=30
b=40

ans1="Addition of",a,"and",b, "is",a+b
print(ans1)

ans2="Addition of a and b is a+b"
print(ans2)

ans3=f"Addition of {a} and {b} is {a+b}"
print(ans3)

