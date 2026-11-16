class BankAccount:
    def __init__(self , balance): 
        self.__balance = balance 

    def get_balance(self):
        return self.__balance

    def set_balance(self , new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else :
            print("INVALID SYNTAX") 

account = BankAccount(500) 
account.set_balance(75621) 
print(account.get_balance())


    

