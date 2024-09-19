#function;
#def:
#This function takes a list of integers as input and returns a list of integers where each element is
#the product of all the elements in the input list up to that index.

#EX1.
'''def greet():               #function declaration
    print ("Hello, World!")   #function body
    print("have a nice day")
    print("welcome")
    
greet()          #function call'''


#EX2.
'''def add():
    a = int(input("Enter the first number:"))
    b = int(input("enter the second number"))
    print("The sum is:",a + b)
add() 
add()
add()
    '''
        
        
        
#EX3.
'''def AreaOfCuboid():
    l=int(input("Enter length:"))
    b=int(input("Enter breadth:"))
    h=int(input("Enter height:"))
    Area=2*(l*b + b*h + h*l)
    print(f"the area of cuboid is:{Area}cu.cm")
    
AreaOfCuboid()'''


#EX4.
'''def AreaOfCuboid():
    l=int(input("Enter length"))
    b=int(input("Enter breadth"))
    h=int(input("Enter height"))
    Area =2*(l*b + b*h + h*l)
print(f"The area of cuboid is: {Area} cu.cm")
AreaOfCuboid()
    
for i in range(3):
    AreaOfCuboid()
    '''
    
    
#EX5.
'''def EvenOdd():
    num=int(input("Enter a number"))
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

EvenOdd() 
EvenOdd()
EvenOdd()   '''


#ex6.
def CalculateBill():
    item=input("Enter the item name:")
    price=float(input("Enter the price of item:"))
    tax=float(input("Enter the tax percentage:"))
    tax_amount=(price * tax)/100
    total_bill=price + tax_amount
    print(f"Your total bill for {item}:{total_bill} Rs")
    
CalculateBill()
