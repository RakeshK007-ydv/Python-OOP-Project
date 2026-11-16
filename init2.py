class Car :
    def __init__(self , brand , model):
        self.brand = brand 
        self.model = model

    def show_details(self,price):
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"Price:{price}")

car1 = Car("TATA" , "MG3")

car1.show_details(90000000)
        