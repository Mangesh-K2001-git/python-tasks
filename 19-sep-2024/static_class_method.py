#class method and Attributes
#class Employee:
ComName ="Microsoft"
def __init__(self, id, salary):
        self.id=id
        self.salary=salary
        
        @classmethod
        def changeCompany(self,newCompany):
            self.ComName=newCompany
            
        Employee.changeCompany("Google")
        Raj= Employee(102,42000)
        print(Raj.ComName)
        
        
            
    #------------------------------------------------------------------       
 
class Employee:
        ComName ="Microsoft"
def __init__(self, id, salary):
        self.id=id
        self.salary=salary
        
        @classmethod
        def changeCompany(self,newCompany):
            self.ComName=newCompany
        @staticmethod
        def show():
            print("This is method of Employee")
            
        Employee.changeCompany("Google")
        Raj= Employee(102,42000)
        print(Raj.ComName)
        
        