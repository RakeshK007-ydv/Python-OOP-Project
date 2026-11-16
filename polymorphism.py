class Animal:
    def make_sound(self):
        print("Animal are making sound loudly") 

class Dog(Animal):
    def make_sound(self):
        print("Dogs are barking ") 

class Cat(Animal):
    def make_sound(self): 
        print("cat is meouing")


animal1= Dog()
animal2 = Cat() 

# animal1.make_sound()
# animal2.make_sound() 

animals = [animal1 , animal2] 

for animal in animals:
    animal.make_sound()
        