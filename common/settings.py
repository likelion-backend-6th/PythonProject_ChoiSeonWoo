import os
from dotenv import load_dotenv


# .env 파일 로드
load_dotenv()


# POSTGRES 설정
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
