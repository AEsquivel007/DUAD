from super_user import SuperUser
from user import User


def main():
    user = User("María")
    super_user = SuperUser("Alberth")
    super_user.access_server()
    super_user.execute_combined_actions()
    
    user.login()
    user.view_profile()
    
    super_user.modify_user_permissions(user)
    super_user.delete_user(user)


if __name__ == '__main__':
    main()