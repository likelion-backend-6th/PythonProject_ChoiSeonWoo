<br>

# 🏬 도서관 관리 콘솔 애플리케이션

<br>

## ❗ 프로젝트 개요
- Python, PosgreSQL을 활용하여 콘솔 기반의 도서관 관리 시스템을 개발
- 이 시스템은 도서 대출, 반납, 그리고 회원 관리 기능을 제공


<br>


## 📑 프로젝트 주요 기능
### 1️⃣ CLI 기반 메뉴
- 사용자는 콘솔을 통해 메뉴를 선택
- 사용자가 선택한 메뉴에 따라 해당 기능을 실행
- 사용자는 메뉴를 통해 프로그램을 종료 가능
- 사용자는 메뉴를 통해 이전 메뉴로 돌아갈 수 있음
- 메뉴 선택 시 콘솔을 삭제하며 사용자가 선택한 메뉴만 출력

### 2️⃣ 데이터 입력 기능
- 사용자는 콘솔을 통해 유저 정보 및 도서의 정보를 입력하고 데이터베이스에 저장
- 사용자 정보는 사용자의 ID, 유저명, 이름, 비밀번호를 포함
- 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함
- 파일을 통해 도서의 정보를 입력하여 데이터베이스에 저장

### 3️⃣ 사용자 정보 기능
- 사용자는 콘솔을 통해 유저명, 이름, 비밀번호를 입력하여 회원가입
- 사용자는 콘솔을 통해 유저명, 비밀번호를 입력하여 로그인
- 로그인 3회 실패 시, 콘솔 접속 종료
- 로그인 상황에서 로그아웃을 입력하여 로그아웃 처리
- 로그아웃 시 초기 메뉴로 돌아감

### 4️⃣ 도서 정보 조회 기능
- 사용자는 도서의 ID 혹은 이름을 입력하여 도서의 정보를 조회
- 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함
- 도서의 상태(대출 가능, 대출 중)가 표시됨.
- 도서의 상태는 도서가 대출 가능한 상태인지, 대출 중인 상태인지를 표현
- 도서가 대출 중인 상태인 경우, 도서의 대출 정보를 함께 출력

### 5️⃣ 도서 대출 기능
- 사용자는 콘솔을 통해 도서의 ID 혹은 이름을 입력하여 도서를 대출
- 대출하면 도서의 상태를 대출 중으로 변경
- 대출 중인 도서를 모두 출력
- 도서가 이미 대출 중일 경우, 대출이 불가능하다고 출력


### 6️⃣ 도서 반납 기능
- 반납 메뉴 선택 시, 사용자의 대출 도서 리스트가 출력됨
- 반납을 원하는 도서의 ID를 입력받아 반납
- 반납하면 도서의 상태가 대출 가능으로 변경
- 반납 처리 후 사용자의 대출 도서 리스트를 출력

### 7️⃣ 대출 정보 조회 기능
- 대출한 도서의 정보를 모두 조회 가능
- 대출 정보는 도서의 ID, 이름, 저자, 출판사, 대출 날짜, 반납일자로 구성
- 대출 정보는 대출 날짜를 기준으로 내림차순으로 정렬

### 8️⃣ 종료 기능
- 사용자는 프로그램을 종료할 수 있음.
- 프로그램 종료 시, 로그아웃 처리

<br>

## 🔧 설치 패키지/모듈 및 실행 환경
|    종류    |       이름        |      버전      |
|:--------:|:---------------:|:------------:|
|    언어    |     python      |     3.10     |
| Database |   PostgreSQL    |     15.3     |
|   IDE    |     Pycharm     | Professional |
|  라이브러리   | psycopg2-bynary |    2.9.6     |
|  라이브러리   |     pandas      |    2.0.3     |
|  라이브러리   |  python-dotenv  |    1.0.0     |


<br>

## 🚀 사용자 흐름
추후 작성 예정

<br>

## 📚 Database ERD
![ERD_library](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/2d654027-7cb1-4993-9d7c-f4a6953a7a3c)



### 🙋‍♂️ 사용자(Users)
| Column Name  |  Data Type   |      Constraint       |
|:------------:|:------------:|:---------------------:|
| **user_id**  |   INTEGER    | PRIMARY KEY, NOT NULL |
| **username** | Varchar(50)  |   UNIQUE, NOT NULL    |
| **fullname** | VARCHAR(50)  |       NOT NULL        |
| **password** | VARCHAR(255) |       NOT NULL        |

### 📕 도서(Books)
| Column Name  |  Data Type   |       Constraint       |
|:------------:|:------------:|:----------------------:|
| **book_id**  |   INTEGER    | PRIMARY KEY, NOT NULL  |
|    **title**     | Varchar(100) |        NOT NULL        |
|    **author**    | VARCHAR(50)  |        NOT NULL        |
|  **publisher**   | Varchar(50)  |        NOT NULL        |
| **is_available** |   BOOLEAN    | NOT NULL, DEFAULT TRUE |

### 🛒 대출(Loans)
| Column Name | Data Type |                   Constraint                    |
|:-----------:|:---------:|:-----------------------------------------------:|
|   **loan_id**   |  INTEGER  |              PRIMARY KEY, NOT NULL              |
|   **user_id**   |  INTEGER  | FOREIGN KEY REFERENCES Users(user_id), NOT NULL |
|   **book_id**   |  INTEGER  | FOREIGN KEY REFERENCES Books(book_id), NOT NULL |
|  **loan_date**  |   DATE    |                    NOT NULL                     |
| **return_date** |   DATE    |                      NULL                       |

<br>

## 추후 업데이트 예정

<br>

