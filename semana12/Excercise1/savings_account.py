from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, min_balance: float, balance = 0):
        super().__init__(owner, balance)
        self.min_balance = min_balance
    
    
    def deposit_money(self, amout:float):
        if amout > 0:
            self.deposit(amout)
        else:
            print("ERROR: Invalid amount to deposit.")
    
    
    def withdraw_money(self, amount:float):
        if amount <= 0:
            print("ERROR: Invalid withdrawal amount!!!")
        else:
            balance = self.get_balance()
            if balance <= self.min_balance:
                print("WARNING: Insufficient funds!!!")
            elif balance - amount < self.min_balance:
                print("WARNING: Insufficient funds. Account's balance can't be lower than 'min balance'.")
            else:
                self.withdraw(amount)
    
    
    def display_balance(self):
        balance = self.get_balance()
        print(f"Account's balance: {balance}")