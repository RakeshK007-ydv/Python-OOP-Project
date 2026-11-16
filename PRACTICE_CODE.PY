class ATM :
    def __init__(self , balance):
        self.balance = balance 

    def check_balance(self):
        return self.balance

account1 = ATM(5000)
account1.check_balance()
print(account1.check_balance())



