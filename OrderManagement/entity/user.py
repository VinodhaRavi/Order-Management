class User:
    def __init__(self, user_id: int, username: str, password: str, role: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role  

    def get_user_id(self):
        return self.user_id
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_role(self):
        return self.role

    def set_user_id(self, user_id):
        self.user_id = user_id
    def set_username(self, username):
        self.username = username
    def set_password(self, password):
        self.password = password
    def set_role(self, role):
        self.role = role
    def __str__(self):
        return f"User[ID={self.user_id}, Username={self.username}, Role={self.role}]"
