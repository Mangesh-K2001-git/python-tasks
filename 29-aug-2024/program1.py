#formulations

'''#(a+b)^2=a*a+b*b+2a*b
a=int(input("Enter the value of a:"))
b=int(input("enter the  value of b:"))
ans=a*a+b*b+2*a*b
print("The value of (a+b)^2 is:",ans)'''


'''#area of circle=3.14*r*r
r=int(input("Enter the radius of r:"))
ans=3.14*r*r
print("The area of circle is:",ans)'''


'''#volume of sphere=(4/3)*3.14*r*r*r
r=int(input("Enter the radius of r:"))   
ans=(4/3)*3.14*r*r*r  
#ans=(4/3)*3.14*(r**3)
print("The volume of sphere is:",ans,"cu.cm")'''


'''#Ex1.To find no.is  prime  or not(no. only divisible  by 1 and itself)

n=int(input("Enter the number:"))
flag=1
for i in range(2,n):
if(n%i==0):
flag=0
break
if(flag==1):
print(n,"is a prime number")
else:
print(n,"is not a prime number")'''


#given no. is palindrome or not(if no. is same if we reverse it)

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")






