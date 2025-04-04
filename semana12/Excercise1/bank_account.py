class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance
    
    
    def deposit(self, amount:float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited amount: {amount}. New account's balance: {self.__balance}")
        else:
            print("WARNING: The amount to deposit must be greater than 0!")
    
    
    def withdraw(self, amount:float):
        if amount > 0:
            if amount > self.__balance:
                print("WARNING: Insufficient funds!!!")
            elif self.__balance - amount < 0:
                print("WARNING: Insufficient funds!!!")
            else:
                self.__balance -= amount
                print(f"Withdrew amount: {amount}. New account's balance: {self.__balance}")
        else:
            print("WARNING: The amount to withdraw must be greater than 0!")
    
    
    def get_balance(self):
        return self.__balance
    
    
    def __str__(self):
        account_details = f"Account's balance: {self.__balance}"
        return account_details