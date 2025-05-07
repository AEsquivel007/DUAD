def is_prime(number_to_validate):
    if number_to_validate < 2:
        return False
    else:
        for number in range(2, int(number_to_validate ** 0.5) + 1):
            if number_to_validate % number == 0:
                return False
    return True


def validate_prime_numbers(list_of_numbers):
    
    if not isinstance(list_of_numbers, list) or not all(isinstance(x, int) for x in list_of_numbers):
        raise TypeError("[WARNING]: The provided list must be a list of integers...!!!")
    
    list_of_prime_numbers = []

    for number in list_of_numbers:
        result = is_prime(number)

        if result == True:
            list_of_prime_numbers.append(number)

    return list_of_prime_numbers


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 25, 67, 70, 71, 72, 73, 89, 90, 96, 97]

result_of_prime_numbers = validate_prime_numbers(list_of_numbers)

print(result_of_prime_numbers)