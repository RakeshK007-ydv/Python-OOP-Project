# my first Git project 

class Payment:
    def pay(self, amount):
        print("Processing payment")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


payment1 = UPI()
payment2 = CreditCard()

payments = [payment1, payment2]

for payment in payments:
    payment.pay(1000)