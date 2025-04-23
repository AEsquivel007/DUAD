

def only_numbers(func):
    def wrapper_only_numbers(*args, **kwargs):
        try:
            if not args:
                raise ValueError("[WARNING]: No arguments were provided...")
            
            if kwargs:
                for key, value in kwargs.items():
                    if not value:
                        raise ValueError(f"[WARNING]: The argument '{key}' must contain a value...")
            
            for index, value in enumerate(args):
                if not isinstance(value, (int, float)):
                    raise TypeError(f"The argument at index: '{index}' with value: '{value}' is not a number...")
                print(f"Valid value: {value}")
            
            return func(*args, **kwargs)
        
        except TypeError as ex:
            print(f"ERROR: {ex}")
        except Exception as ex:
            print(f"Idenfitied error: {ex}")
    
    return wrapper_only_numbers


@only_numbers
def receive_values(*args, **kwargs):
    print(f"The positional arguments received by the function were: {args}")
    print(f"The keyword arguments received by the function were: {kwargs}")


receive_values(1,2,3,4,5,6,7,8,9, name="Alberth")