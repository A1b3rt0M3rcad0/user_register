from datetime import datetime

class Users:

    def __init__(self, username:str, password:str, created_at:datetime) -> None:
        self.username = username
        self.password = password
        self.created_at = created_at