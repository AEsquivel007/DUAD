import pytest
from week16.methods_to_test.exercise_4 import reverse_a_string


def test_reverse_a_string():
    string_to_reverse = "Hello world"
    
    reversed_string = reverse_a_string(string_to_reverse)
    
    assert reversed_string == "dlrow olleH"


def test_reverse_a_string_with_empty_argument():
    string_to_reverse = ""
    
    reversed_string = reverse_a_string(string_to_reverse)
    
    assert reversed_string == ""


def test_reverse_a_string_throws_exception_without_string_argument():
    numbers_to_reverse = 12345678
    
    with pytest.raises(TypeError):
        reverse_a_string(numbers_to_reverse)