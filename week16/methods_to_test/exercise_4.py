def reverse_a_string(string_to_reverse):
        if not isinstance(string_to_reverse, str):
                raise TypeError("[WARNING]: The provided argument must be a string...!!!")
        
        reversed_string = ""
        for char in string_to_reverse[::-1]:
                reversed_string += char
        return reversed_string


string_to_reverse = "Hello world"

reversed_string = reverse_a_string(string_to_reverse)

print(f'Provided string: "{string_to_reverse}", reversed string: "{reversed_string}"')