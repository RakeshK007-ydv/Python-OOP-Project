class Employee :
    def __init__(self, name , age , salary , department):
        self.name = name 
        self.age = age 
        self.salary = salary 
        self.department = department 

employee1 = Employee("Rakesh" , 21 , 60000 , "PSPCL") 
employee2 = Employee("Vansh" , 21, 50000 , "Sales") 
employee3 = Employee("Aman" , 18 , 15000 , "Shop")

print(employee1.name)
print(employee1.age)
print(employee1.salary)
print(employee1.department)

print(employee2.name)        
print(employee2.age)        
print(employee2.salary)        
print(employee2.department) 

print(employee3.name)
print(employee3.age)
print(employee3.salary)
print(employee3.department)