from abc import ABC , abstractmethod 
from datetime import datetime 

class BankAccount(ABC):
    def __init__(self, name , balance):
        self.name = name 
        self.__balance = balance 
        self.transaction = []

    def get_balance(self):
        return self.__balance 
    
    def set_balance(self, new_balance):
        self.__balance = new_balance   

    @abstractmethod
    def withdraw(self , amount):
        pass 

    def check_balance(self):
        print(f"Name:, {self.name}")
        print(f"current balance:, {self.__balance}") 

    def transaction_history(self):
        for transaction in self.transaction :
         print(transaction)

    #Child class 
class SavingBankAccount(BankAccount): 
        def withdraw(self, amount):
            current_balance = self.get_balance()
            if amount <= 0 :
                print("Invalid withrawn amount")
            elif amount > current_balance :
                print("insufficinet withrawn balance , aukaat me reh lode ")
            else:
                new_balance = current_balance - amount 
                self.set_balance(new_balance)
                current_time = datetime.now()
                formatted_time = current_time.strftime("%d-%m-%Y %I:%M %p")
                self.transaction.append(f"Transaction Withraw: {amount} | {formatted_time}") 
                print(f"Withraw:{amount} successfully") 

        #depsoite money in account
        def deposit(self , amount): 
            current_balance = self.get_balance()
            if amount > 0 :
                new_balance = current_balance + amount 
                self.set_balance(new_balance)
                current_time = datetime.now()
                formatted_time = current_time.strftime("%d-%m-%Y %I:%M %p")
                self.transaction.append(f"Transaction Deposited : {amount} | {formatted_time} ")
                print(f"Deposited:{amount} successfully") 
            else:
                print("INVALID SYNTAX0") 



Account1 = SavingBankAccount("Rakesh" , 4000) 
while True :
    print("\n====Rakesh Bank=====")
    print("1. Check Balance")
    print("2. Withraw Balance")
    print("3. Deposit Balance")
    print("4. Transaction History")
    print("5. Exit") 
    choice = input("Enter Your Choice:=")  
    if choice == "1":
        Account1.check_balance() 

    elif choice == "2":
        amount =float(input("enter your deposit amount:"))
        Account1.deposit(amount) 

    elif choice =="3":
        amount =float(input ("enter your withraw amount:"))
        Account1.withdraw(amount)


    elif choice == "5":
        print("Thank you for using Rakesh Bank!")
        break

    else:
        print("Invalid choice!")
  
# Account1 = SavingBankAccount("Aman" , 3000) 
# Account1.check_balance()
# Account1.deposit(6000)
# Account1.check_balance()
# Account1.transaction_history()
            



    



