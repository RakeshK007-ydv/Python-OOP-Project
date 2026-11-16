class Person:
    def __init__ (self, name , age ):
        self.name = name 
        self.age = age 

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary 

    def show_details(self,):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Salary:{self.salary}") 
        print("he is working so hard to get fuck by god ")

person1 = Employee("Rakesh" , 21 , 150000) 

person1.show_details()




