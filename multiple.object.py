class Dog:
    def name(self , name ):
        self.name = name 
        

dog1 = Dog()
dog2 = Dog() 

dog1.name("Tommy")
dog2.name("Bruno")


print(dog1.name)
print(dog2.name)