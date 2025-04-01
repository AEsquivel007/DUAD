from savings_account import SavingsAccount


def main():
    try:
        print("Welcome to Lyfter's Bank System:\n")
        
        while True:
            name = input("Provide the name of the account's owner: ")
            if name.replace(" ", "").isalpha():
                break
            print("WARNING: The name of the account's owner must contain only strings!!!")
        
        while True:
            min_balance_value = input(f"Please define the minimum balance for the account: ")
            if min_balance_value.isdigit():
                min_balance = float(min_balance_value)
                break
            print("WARNING: The minimum balance to define must contain only numeric values!!!")
        
        account = SavingsAccount(name, min_balance)
        
        while True:
            print("""Lyfter's Bank Menu, below you can see the available options:
                1. Deposit money
                2. Withdraw money
                3. Balance
                4. Exit""")
            
            given_option:str = input("Select one of the given options (Insert the number of the desired option): ")
            
            if given_option.isdigit():
                option = int(given_option)
                
                if option > 0 and option <5:
                    match option:
                        case 1:
                            amount = float(input("Provide the amount to deposit: "))
                            account.deposit_money(amount)
                        case 2: 
                            amount = float(input("Provide the amount to withdraw: "))
                            account.withdraw_money(amount)
                        case 3:
                            account.display_balance()
                        case 4:
                            print("Thank you for using the Lyfter's Bank System!!!")
                            exit()
                else:
                    print("WARNING: The provided number is not related to a valid option!!!\n")
            else:
                print("ERROR: Only integers are allowed!!!")
            
            match option:
                case "1":
                    amount = input()
    
    except Exception as ex:
        print("ERROR: An unexpected error occurred.")
        print(f"System error: {ex}")
        exit()


if __name__ == '__main__':
    main()