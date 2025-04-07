

def only_numbers(func):
    def wrapper_only_numbers(*args):
        try:
            if len(args) < 1:
                raise ValueError("[WARNING]: No arguments were provided...")
            
            for index, value in enumerate(args):
                if not isinstance(value, (int, float)):
                    raise TypeError(f"The argument {args[index]} with value: '{value}' is not a number...")
                print(f"Valid value: {value}")
            
            return func(*args)
        
        except TypeError as ex:
            print(f"ERROR: {ex}")
        except Exception as ex:
            print(f"Idenfitied error: {ex}")
            
    return wrapper_only_numbers


@only_numbers
def receive_values(*args):
    print(f"The received values in the function were: {args}")


receive_values(1,2,3,4,5,6,7,8,9)
#receive_values(1,2,3,5,"Hello",8)