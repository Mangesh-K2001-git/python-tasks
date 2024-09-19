#ex1.
'''def percentage():
    marks = [80,34,76,94,97]
    count = len(marks)
    total = sum(marks)
    
    
    print(f"Total obtained marks:{total}")
    print(f"percentage:{round(total/count,2)}")
percentage()'''
    

def percentage():
    marks= [80,67,93,97 ,78]
    count =len(marks)
    total = 0
    for marks in marks:
        total +=marks
        
        print(f"total obtained marks:{total}")
        print(f"percentage:{round(total/count,2)}")

percentage()
    
    
    
        
