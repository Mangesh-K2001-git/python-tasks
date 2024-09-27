#function parameters
#default arguments
#args and kwargs
#lambda function




#args and kwargs
#ex1.args
def add(*digits):
    print(digits)
    sum=0
    for i in digits:
        sum+=i
        
    print(sum)
add(2,3,4,543,5678,12,3,78,99)

#EX2.kwargs
def Percentage(**marks):
    total=0
    for sub in marks:
        total +=marks[sub]
    print(f"Total marks:{total} OutOf 600")
    per=( total /600)*100

    print(f"Percentage:{round(per,2)}%")

Percentage(maths=99,eng=85,sci=92,marathi=71,SocialSci=86)
Percentage(maths=99,eng=85,sci=92,it=180,evs=98)
Percentage()

#lambda function
#EX1.
Squ=lambda X:X**2
print(Squ(5))
print(Squ(8))
print(Squ(99))

#ex2.
isEven=lambda x:x%2==0
print(isEven(10))
print(isEven(35))

#ex3.
isEven=lambda x:"even" if(x%2==0) else "odd"
print(isEven(10))
print(isEven(35))

#ex4.
sqr=lambda x:print(f"squ of {x} is {x**2}")
sqr(36)

#ex5.
Add=lambda myList:sum(myList)
print(add(2,3,4))
    