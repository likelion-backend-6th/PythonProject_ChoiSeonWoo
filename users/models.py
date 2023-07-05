from typing import Optional

from common.database import DatabaseManager, postgres, PostgreSQL


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

    def get(self, size: Optional[int] = None):
        if self.username != None:
            query = f"SELECT * from users WHERE username = '{self.username}';"
            user = DatabaseManager(postgres, self.table, query).fetch_one()
            return user
        elif size:
            query = f"SELECT * from users order by id limit {size};"
            users = DatabaseManager(postgres, self.table, query).fetch_many(size)
            return users
        else:
            query = "SELECT * from users order by id;"
            users = DatabaseManager(postgres, self.table, query).fetch_all()
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


# 모든 유저 조회
users = Users()
all_users = users.get()
print(f"all_users: {all_users}")

# 일부 유저 조회
users = Users()
multiple_users = users.get(3)
print(f"multiple_users: {multiple_users}")


# 특정 유저 조회
users = Users("admin")
single_user = users.get()
print(f"single_user: {single_user}")