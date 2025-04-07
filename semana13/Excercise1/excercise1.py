
def decorator(func):
    def wrapper_decorator(*args):
        
        print("Starting decorator")
        
        a, b = args
        print(f"Printing first argument of the decorated fuction: {a}")
        print(f"Printing second argument of the decorated fuction: {b}")
        
        result = func(*args)
        
        print(f"Printing the returned value of the decorated function: {result}")
        print("Finishing decorator")
        
        return result
    
    return wrapper_decorator

@decorator
def add_numbers(num1:int, num2:int):
    result = num1 + num2
    print(f"Calculating the result of {num1} + {num2}...")
    return result


sum = add_numbers(10, 15)
print(f"The result is: {sum}")
