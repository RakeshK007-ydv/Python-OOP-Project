class Animal :
    def make_sound(self):
        print("Animal makes a sound")

class Dog (Animal):
    def make_sound(self): 
        super().make_sound()
        print("Dogs are barking so hard and pooping so bad ") 

animal1 = Dog()
animal1.make_sound()
        