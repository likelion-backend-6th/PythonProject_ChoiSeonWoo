import os
from dotenv import load_dotenv


# .env 파일 로드
load_dotenv()


# POSTGRES 설정
postgres_host = os.getenv("POSTGRES_HOST")
postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
