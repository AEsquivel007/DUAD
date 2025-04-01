from user import User
from administrator import Administrator


class SuperUser(User, Administrator):
    pass