from typing import Optional


class Users:
    def __init__(self,
                 username: Optional[str] = None,
                 fullname: Optional[str] = None,
                 password: Optional[str] = None
                 ):
        self.table = "users"
        self.username = username
        self.fullname = fullname
        self.password = password