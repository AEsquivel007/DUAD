""" 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
        a. Pista: investigue de que otras maneras se puede usar el `range`. """

string_to_reverse = 'Alberth Esquivel'

# 1. Reversando un string con un "range()" usando un "for in" loop

reversed_string_value = ''
for value in range(len(string_to_reverse)-1,-1,-1):
    reversed_string_value +=string_to_reverse[value]

print (reversed_string_value)

print('-------------------------------------------------------------------------------------')

# 2. Reversando un string con el método de slice [#::#]

reversed_string = string_to_reverse[::-1]

print(reversed_string)


print('-------------------------------------------------------------------------------------')

# 3. Reversando un string con un "for in" loop

reversed_value = ''
for character in string_to_reverse:
    reversed_value = character + reversed_value 

print(reversed_value)

print('-------------------------------------------------------------------------------------')

# 4. Revesando un string con un "for in" loop y método "reversed()"

reversed_method_result = ''
for char in reversed(string_to_reverse):
    reversed_method_result += char

print(reversed_method_result)    

print('-------------------------------------------------------------------------------------')

