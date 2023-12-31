import os
from dotenv import load_dotenv


# .env 파일 로드
load_dotenv()


# debug 모드
DEBUG = False


# 관리자 계정
ADMIN_USER_ID_LIST = os.getenv("ADMIN_USER_ID_LIST")
ADMIN_USER_ID_LIST = list(map(int, ADMIN_USER_ID_LIST.split(",")))


# POSTGRES 설정
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# DB TABLE 설정
CREATE_USER_TABLE = """   CREATE TABLE IF NOT EXISTS users ( 
       id SERIAL PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       fullname VARCHAR(50) NOT NULL,
       password VARCHAR(255) NOT NULL
   );"""

CREATE_BOOK_TABLE = """   CREATE TABLE IF NOT EXISTS books (
       id SERIAL PRIMARY KEY,
       title VARCHAR(100) NOT NULL,
       author VARCHAR(50) NOT NULL,
       publisher VARCHAR(50) NOT NULL,
       is_available BOOLEAN NOT NULL DEFAULT TRUE
   );"""

CREATE_LOAN_TABLE = """   CREATE TABLE IF NOT EXISTS loans (
       id SERIAL PRIMARY KEY,
       user_id INTEGER NOT NULL,
       book_id INTEGER NOT NULL,
       loan_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
       return_date TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
       FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
   );"""

TABLES = ["users", "books", "loans"]
CREATE_QUERY_LISTS = [CREATE_USER_TABLE, CREATE_BOOK_TABLE, CREATE_LOAN_TABLE]
