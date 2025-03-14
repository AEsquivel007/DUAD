""" 1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
            a. Ejemplos:
            b. `first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
            `second_list = ["casos", "los", "la", "por", "es", "util"] ->
            Hay casos
            en los
            que la
            iteracion por
            indice es
            muy util """

first_list = ["Hay", "en", "que", "iteración", "índices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "útil"]

for index in range(0, len(first_list)):
    element_in_first_list = first_list[index]
    element_in_second_list = second_list[index]
    
    print(f'{element_in_first_list} {element_in_second_list}')