def order_words_alphabetically_of_a_given_string(phrase):
        
        if not isinstance(phrase, str):
                raise TypeError("[WARNING]: Only strings are allowed...!!!")
        
        list_of_words = phrase.rsplit("-") 

        list_of_words.sort()

        separator = "-"
        ordered_string = separator.join(list_of_words)

        return ordered_string


ordered_string = order_words_alphabetically_of_a_given_string("python-variable-function-computer-monitor")

print(ordered_string)