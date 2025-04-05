from user import User
from administrator import Administrator


class SuperUser(User, Administrator):
    
    def __init__(self, name):
        super().__init__(name)
    
    
    def access_server(self):
        print(f"{self.name} with SuperUser role accessed the server.")
    
    
    def execute_combined_actions(self):
        print(f"{self.name} as SuperUser started the execution of combining multiple actions based on different roles:")
        self.login()
        self.view_profile()
        self.access_server()
        print(f"{self.name} as SuperUser finished the execution of combining multiple actions based on different roles:")