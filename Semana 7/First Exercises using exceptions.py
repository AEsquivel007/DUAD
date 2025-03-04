def validate_give_number_is_100(value:int):
    if value < 100:
        raise ValueError('The given number is lower than 100!!!')
    elif value > 100:
        raise ValueError('The given number is higher than 100!!!')
    return True


def main():
    try:
        given_number = input('Please, insert a number: ')
        number = int(given_number)
        validate_give_number_is_100(number)
    except Exception as ex:
        print(ex)
        exit()


if __name__ == '__main__':
    main()