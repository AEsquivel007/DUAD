class Administrator:
    
    def delete_user(self, user):
        print(f"User {user.name} has been deleted by an Administrator.")
    
    
    def modify_user_permissions(self, user):
        print(f"{user.name}'s permissions has been changed by an Administrator.")