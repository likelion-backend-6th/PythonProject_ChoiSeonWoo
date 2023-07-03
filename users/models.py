from typing import Optional

from common.database import DatabaseManager, postgres


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

    def get(self):
        if self.username != None:
            query = f"SELECT * from users WHERE username = '{self.username}';"
        else:
            query = "SELECT * from users;"
        users = DatabaseManager(postgres, self.table, query).fetch_query()
        return users

    def post(self):
        query = f"""
        INSERT INTO users (username, fullname, password)
        VALUES ('{self.username}', '{self.fullname}', '{self.password}')
        """
        DatabaseManager(postgres, self.table, query).execute_query()