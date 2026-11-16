class Vehicle:
    def start(self):
        print("Vehicle is starting") 

class Car(Vehicle):
    def start(self):
        print("Car is starting with a Key") 

vehicle1 = Car()

vehicle1.start()