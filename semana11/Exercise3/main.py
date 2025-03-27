import utilities


def main():
    try:
        while True:
            utilities.display_menu()
            result = utilities.ask_if_continue()
            
            if not result:
                print("Thank you for using the system. Bye...")
                break
        
    except Exception as ex:
        print("ERROR: An unexpected error occurred.")
        print(f"System error: {ex}")
        exit()


if __name__ == '__main__':
    main()