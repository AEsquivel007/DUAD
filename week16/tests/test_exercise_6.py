import pytest
from week16.methods_to_test.exercise_6 import order_words_alphabetically_of_a_given_string


def test_order_words_alphabetically_of_a_given_string():
    phrase = "python-variable-funcion-computadora-monitor"
    
    ordered_string = order_words_alphabetically_of_a_given_string(phrase)
    
    assert ordered_string == "computadora-funcion-monitor-python-variable"


def test_order_words_alphabetically_of_a_given_string_with_empty_argument():
    phrase = ""
    
    ordered_string = order_words_alphabetically_of_a_given_string(phrase)
    
    assert ordered_string == ""


def test_order_words_alphabetically_of_a_given_string_with_numbers():
    phrase = 3245265647564
    
    with pytest.raises(TypeError):
        order_words_alphabetically_of_a_given_string(phrase)