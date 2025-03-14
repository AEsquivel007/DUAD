""" 
1. string + string → ?
2. string + int → ?
3. int + string → ?
4. list + list → ?
5. string + list → ?
6. float + int → ?
7. bool + bool → ? """

# 1. string + string → concatena ambos strings
string1 = 'Alberth'
string2 = 'Esquivel'
print(string1 + string2)

# 2. string + int → TypeError: can only concatenate str (not "int") to str
int1 = 1
print(string1 + int1)

# 3. int + string → TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(int1 + string1)

# 4. list + list → Unifica ambas listas en una sola lista.
my_first_list = [1,2,3]
my_second_list = [3,2,1,]
print(my_first_list + my_second_list)

# 5. string + list → TypeError: can only concatenate str (not "list") to str
print(string1 + my_first_list)

# 6. float + int or int + float → Para ambos casos se suman los valores del int y float.
float1 = 3.14
print(int1 + float1 + int1)

# 7. bool + bool → Dicha combinación suma los valores de True y False, donde True = 1 y False = 0.
bool1 = True
bool2 = True
print(bool1 + bool2)