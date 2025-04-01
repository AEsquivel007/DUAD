from super_user import SuperUser


def main():
    super_user = SuperUser("Alberth")
    super_user.print_name()
    super_user.delete_user(super_user.name)


if __name__ == '__main__':
    main()