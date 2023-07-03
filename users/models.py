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
        users.sort(key=lambda x:x[0])
        return users

    def post(self):
        query = f"""
        INSERT INTO users (username, fullname, password)
        VALUES ('{self.username}', '{self.fullname}', '{self.password}')
        """
        DatabaseManager(postgres, self.table, query).execute_query()

    def put(self, new_fullname: str, new_password: Optional[str] = None):
        if new_password:
            query = f"""
            UPDATE users SET fullname = '{new_fullname}', password = '{new_password}'
            WHERE username = '{self.username}';
            """
        else:
            query = f"""
            UPDATE users SET fullname = '{new_fullname}'
            WHERE username = '{self.username}';
            """
        DatabaseManager(postgres, self.table, query).execute_query()
