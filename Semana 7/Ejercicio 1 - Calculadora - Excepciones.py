""" Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación. """

def add_numbers(current_number:int, given_number:int):
    result = current_number + given_number
    print(f"The result of {current_number} + {given_number} is: {result}")
    return result


def subtract_numbers(current_number:int, given_number:int):
    result = current_number - given_number
    print(f"The result of {current_number} - {given_number} is: {result}")
    return result


def multiply_numbers(current_number:int, given_number:int):
    result = current_number * given_number
    print(f"The result of {current_number} * {given_number} is: {result}")
    return result


def divide_numbers(current_number:int, given_number:int):
    if current_number == 0 or given_number == 0:
        print("Divisions by zero can't be executed")
    else:
        result = current_number / given_number
        print(f"The result of {current_number} / {given_number} is: {result:.2f}")
        return result


def clean_result():
    aux_number:int = 10
    print("The result was deleted!!!")
    return aux_number


def select_operation(operation:int, current_number:int = None, given_number:int = None):
    match operation:
        case 1:
            result = add_numbers(current_number, given_number)
            return result
        case 2:
            result = subtract_numbers(current_number, given_number)
            return result
        case 3:
            result = multiply_numbers(current_number, given_number)
            return result
        case 4:
            result = divide_numbers(current_number, given_number)
            return result
        case 5:
            result = clean_result()
            return result


def calculator_system():
    current_number:int = 10
    continue_with_operations = True

    while(continue_with_operations):
        try:
            print("""Welcome to the Lyfter's Calculator System, below you can see the available operations:
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Delete result""")
            operation = int(input("Please, insert the number of the operation that you'd like to execute: "))

            if operation > 0 and operation < 6:
                if operation == 5:
                    result = select_operation(operation)
                    current_number = result
                else:
                    try:
                        print(f"[IMPORTANT: Default value of the first number given by the application is: {current_number}]")
                        given_number = int(input("Please insert the value of the second number to execute the desired operation: "))

                        result = select_operation(operation, current_number, given_number)
                        current_number = result

                    except ValueError as ex:
                        print("The given number to perform the selected operation is invalid!!!")                    
            else:
                print("The given number is out of the range. -> Valid range is from 1 to 5")
                exit()

        except ValueError as ex:
            print(f"Error when selecting one of the given operations.")
            print(f"Identified error: {ex}")

        decision = input("Would you like to execute another operation? (yes/no): ")

        if(decision == "yes"):
            print("Good choise!!!")
        elif(decision == "no"):
            continue_with_operations = False
        else:
            print("Invalid argument. Bye!!!")
            exit()

    else:
        print("Thank you for using the Lyfter's Calculator System!!!")
        exit()


def main():
    try:
        calculator_system()
    except Exception as ex:
        print(ex)
        exit()


if __name__ == "__main__":
    main()