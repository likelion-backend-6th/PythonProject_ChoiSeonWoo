from typing import Optional, Tuple

from common.database import DatabaseManager


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

    def get(self,
            size: Optional[int] = None,
            id: Optional[int] = None,
            username: Optional[str] = None,
            fullname: Optional[str] = None,
            order_by_info: Tuple = ('id', 'ASC')
    ):
        query = "SELECT * FROM users "
        extra_query = []

        if id:
            extra_query.append(f"id = '{id}'")
        if username:
            extra_query.append(f"username = '{username}'")
        if fullname:
            extra_query.append(f"fullname = '{fullname}'")

        extra_query = "WHERE " + " AND ".join(extra_query) if extra_query else ""

        if order_by_info:
            extra_query += f" ORDER BY {order_by_info[0]} {order_by_info[1]}"

        query += extra_query

        limit_query = f" LIMIT {size};" if size else ";"
        query += limit_query

        users = DatabaseManager(self.table, query).fetch_all()
        return users

    def post(self):
        query = f"""
        INSERT INTO users (username, fullname, password)
        VALUES ('{self.username}', '{self.fullname}', '{self.password}')
        """
        DatabaseManager(self.table, query).execute_query()

    def put(self,
            fullname: str,
            id: Optional[int] = None,
            username: Optional[str] = None,
            password: Optional[str] = None
    ):
        query = f"UPDATE users SET fullname = '{fullname}' "

        if password:
            query += f", password = '{password}'"

        if id:
            query += f"WHERE id = {id}"
        elif username:
            query += f"WHERE username = '{username}"

        query += ";"

        DatabaseManager(self.table, query).execute_query()

    def handle_complex_query(
            self,
            query: str,
            handle_type: str
    ):
        if handle_type == "get":
            result = DatabaseManager(self.table, query).fetch_all()
        elif handle_type == "post" or "put":
            result = DatabaseManager(self.table, query).execute_query()
        print(f"'{handle_type}' Request was processed Successfully")
        return result
