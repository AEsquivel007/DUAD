""" 2. Experimente con el concepto de scope:
        1. Intente accesar a una variable definida dentro de una función desde afuera.
        2.  Intente accesar a una variable global desde una función y cambiar su valor. """

my_global_variable = "Alberth"


def my_function():
    print(f'Accesando a la variable global: {my_global_variable}')


def access_to_global_variable_and_modify_it():
    my_function()
    global my_global_variable 
    my_global_variable = "Contenido modificado..."
    print(f'Imprimiendo el valor modificado de la variable global: {my_global_variable}')


access_to_global_variable_and_modify_it()
# Sin usar el keyword "global" y al tratar de modificarla adentro de una función me tira el error:
#   "UnboundLocalError: cannot access local variable 'my_global_variable' where it is not associated with a value"

# Para poder modificar el valor de una variable global, primero debemos usar el keyword "global" y el nombre de la 
#   variable global para poder tener el acceso a modificar dicho valor gobal y luego podemos asignar el nuevo valor con "="