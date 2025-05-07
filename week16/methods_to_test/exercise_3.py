def sum_numbers(list_of_numbers):
        if not isinstance(list_of_numbers, list) or not all(isinstance(x, int) for x in list_of_numbers):
                raise TypeError("[WARNING]: The provided list must be a list of integers...!!!")
        
        total = 0
        for number in list_of_numbers:
                total += number
        return total


list_of_numbers = [1, 1, 1, 1, 1, 4, 6, 1, 1, 1, 1, 1, 2, 29, 1, 1, 1, 1, 1]

sum_of_all_numbers = sum_numbers(list_of_numbers)

print(f'The total is: {sum_of_all_numbers}')