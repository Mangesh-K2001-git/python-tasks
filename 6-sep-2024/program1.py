#inheritance
#def-class can inherit properties  and methods from another class using the (class_name) syntax.


class Computer:
    def __init__(self, ip,pro, op,price,os):
        self.input_device=ip
        self.processing_unit=pro
        self.output_device=op
        self.price=price
        self.operating_system=os
        
        def display_details(self):
            print("Input Device:", self.input_device)
            print("Processing Unit: ",self.processing_unit)
            print("Output Device:", self.output_device)
            print("Price:" ,self.price)
            print("Operating System: ",self.operating_system)
            
        
com= Computer (["keyboard","mouse"],"cpu-intel-i5",["monitor","speakers"],35500,"window")
com.display_details() 
print()

com1=Computer (["keyboard","mouse"],"cpu-intel-i9",["monitor","speakers"],55500,"window")
com1.display_details()
print()



        