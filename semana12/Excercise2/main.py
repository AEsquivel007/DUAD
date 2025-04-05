from circle import Circle
from rectangle import Rectangle
from square import Square


def main():
    try:
        while True:
            print("""Welcome to Lyfter's Shape System, below you can see the available options:
                1. Circle
                2. Rectangle
                3. Square
                4. Exit""")
            
            given_option:str = input("Select one of the given options to calculate its area and perimeter: ")
            
            if given_option.isdigit():
                option = int(given_option)
                
                if option > 0 and option <5:
                    match option:
                        case 1:
                            radius = float(input("Provide the radius of the circle: "))
                            circle = Circle(radius)
                            area = circle.calculate_area()
                            perimeter = circle.calculate_perimeter()
                            print(f"The circle with a radius of: {radius}, has an area of: {area} and a perimeter of: {perimeter}.")
                        case 2: 
                            length = float(input("Provide the length of the rectangle: "))
                            width = float(input("Provide the width of the rectangle: "))
                            rectangle = Rectangle(length, width)
                            area = rectangle.calculate_area()
                            perimeter = rectangle.calculate_perimeter()
                            print(f"The rectangle with a length of: {length} and a width of: {width} has an area of: {area} and a perimeter of: {perimeter}.")
                        case 3:
                            length_side = float(input("Provide the side's length of the square:"))
                            square = Square(length_side)
                            area = square.calculate_area()
                            perimeter = square.calculate_perimeter()
                            print(f"The square with a side's length of: {length_side} has an area of: {area} and a perimeter of: {perimeter}.")
                        case 4:
                            print("Thank you for using the Lyfter's Shape System!!!")
                            exit()
                else:
                    print("WARNING: The provided number is not related to a valid option!!!\n")
            else:
                print("ERROR: Only integers are allowed!!!")
    
    except Exception as ex:
        print("ERROR: An unexpected error occurred.")
        print(f"System error: {ex}")
        exit()


if __name__ == '__main__':
    main()