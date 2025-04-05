class User:
    
    def __init__(self, name):
        self.name = name
    
    
    def login(self):
        print(f"User {self.name} logged in with User role.")
    
    
    def view_profile(self):
        print(f"{self.name}'s profile displayed successfully.")