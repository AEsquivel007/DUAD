import pytest
from week16.methods_to_test.exercise_3 import sum_numbers


def test_sum_numbers():
    list_of_numbers = [1, 1, 1, 1, 1, 4, 6, 1, 1, 1, 1, 1, 2, 29, 1, 1, 1, 1, 1]
    
    result = sum_numbers(list_of_numbers)
    
    assert result == 56


def test_sum_numbers_with_empty_list():
    list_of_numbers = []
    
    result = sum_numbers(list_of_numbers)
    
    assert result == 0


def test_sum_numbers_throws_exception_without_only_numbers():
    list_of_sum = [6, 1, "Hello", "World"]
    
    with pytest.raises(TypeError):
        sum_numbers(list_of_sum)