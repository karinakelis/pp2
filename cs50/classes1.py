class Employee:
    def __init__(self,first,last,pay):   #initialize method
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comany.com'
        
        #method
        def fullname(self):
            return '{} {}'.forma(self.first,self.last)
        
        
emp_1 = Employee('Karina','Kelis',80000)
emp_2 = Employee('Aruna','YUu',800000)

print(emp_1.email)
print(emp_2.email)
#print(emp_1.fullname())
print(Employee.fullname(emp_1))



