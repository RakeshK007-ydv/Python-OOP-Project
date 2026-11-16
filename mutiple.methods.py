class ATM:
    def __init__(self , balance):
        self.balance = balance 

    def check_balance(self):
        print(f"currant balance: {self.balance}")

    def deposite_amount(self,amount):
        self.balance+=amount
        print(f"deposite: {amount}") 
        
    def withrawl_amount(self,amount):
        self.balance-=amount
        print(f"withrawl: {amount}") 

account1 = ATM(6000)

account1.check_balance()
account1.deposite_amount(2000)
account1.withrawl_amount(2000)
account1.check_balance()


          