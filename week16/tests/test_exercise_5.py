import pytest
from week16.methods_to_test.exercise_5 import count_upper_or_lower_case_words


def test_count_upper_or_lower_case_words():
    phrase = "I love Nación Manga - Alberth Esquivel Alvarado - Ríos"
    
    result = count_upper_or_lower_case_words(phrase)
    
    assert result == "There's 7 upper cases and 36 lower cases"


def test_count_upper_or_lower_case_words_with_empty_string():
    phrase = ""
    
    result = count_upper_or_lower_case_words(phrase)
    
    assert result == "There's 0 upper cases and 0 lower cases"


def test_count_upper_or_lower_case_words_from_not_string():
    phrase = 12083420481058432
    
    with pytest.raises(TypeError):
        count_upper_or_lower_case_words(phrase)