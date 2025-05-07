def count_upper_or_lower_case_words(phrase:str):
  counter_of_upper_case_words = 0
  counter_of_lower_case_words = 0

  for character in phrase:
      if character.isupper():
          counter_of_upper_case_words += 1
      elif character.islower():
          counter_of_lower_case_words += 1

  text_to_return = (f"There's {counter_of_upper_case_words} upper cases and {counter_of_lower_case_words} lower cases")
  
  return text_to_return


phrase = "I love Nación Manga - Alberth Esquivel Alvarado - Testing"

value_to_print = count_upper_or_lower_case_words(phrase)

print(value_to_print)