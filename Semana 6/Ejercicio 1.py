""" Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda. """

def first_function():
    print('Invocando la segunda función: ')
    second_function()


def second_function ():
    print('Hello world!')


first_function()