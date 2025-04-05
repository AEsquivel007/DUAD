import menu


def display_menu():
    try:
        print("""Welcome to Lyfter's Bank System, below you can see the available options:
            1. Deposit money
            2. Withdraw money
            3. Balance""")
        
        given_option:str = input("Select one of the given options (Insert the number of the desired option): ")

        if given_option.isdigit():
            option = int(given_option)

            if option > 0 and option < 3:
                menu.select_option(option)
            else:
                print("WARNING: The provided number is not related to a valid option. The valid numbers to provide are: 1 and 2!!!")
        else:
            print("ERROR: Only integers are allowed!!!")
    
    except ValueError as ex:
        print("ERROR: An unexpected error occurred when selecting the options!!!")
        print(f"System error: {ex}")
        exit()


def ask_if_continue():
    try:
        while True:
            user_input = input("Would you like to continue using the system, (s/n)?: ")
            
            if user_input not in ["s","n"]:
                print("ERROR: The valid options are: (s) and (n)...")
            elif user_input == "s":
                return True
            else:
                return False

    except:
        print("ERROR: An unexpected error occurred with the exectution of the system!!!")