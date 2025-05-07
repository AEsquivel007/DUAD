import pytest
from week16.methods_to_test.exercise_7 import validate_prime_numbers


def test_validate_prime_numbers():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 25, 67, 70, 71, 72, 73, 89, 90, 96, 97]
    
    result_of_prime_numbers = validate_prime_numbers(list_of_numbers)
    
    assert result_of_prime_numbers == [2, 3, 5, 7, 11, 13, 67, 71, 73, 89, 97]


def test_validate_prime_numbers_with_empty_list():
    list_of_numbers = []
    
    result_of_prime_numbers = validate_prime_numbers(list_of_numbers)
    
    assert result_of_prime_numbers == []


def test_validate_prime_numbers_with_only_strings():
    list_of_numbers = ["Hello", "world", "Bye"]
    
    with pytest.raises(TypeError):
        validate_prime_numbers(list_of_numbers)