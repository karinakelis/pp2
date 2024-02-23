'''class Employee:
   
   vari = 10.68
   def __init__(self,first,last,pay):
    self.pay = pay
    
def aplly_raise(self):
    self.pay = int(self.pay * Employee.vari)   
    
print() '''


#classmethods and staticmethods

class Employee:
    def __init__(self,first,last,pay):   #initialize method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comany.com'
        
        #method
        def fullname(self):
            return '{} {}'.forma(self.first,self.last)
        
        @classmethod
        def set_raise_amt(cls, amount):  #cant use word class
            cls.raise_amt = amount
        
        
emp_1 = Employee('Karina','Kelis',80000)
emp_2 = Employee('Aruna','YUu',800000)


Employee.set_raise_amt(1.05)
#print(emp_1.email)
#print(emp_2.email)
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))
print(Employee.raise_amt)
print(emp_1.raise_amt)




    