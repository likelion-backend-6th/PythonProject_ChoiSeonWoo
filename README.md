<br>

# 🏬 도서관 관리 콘솔 애플리케이션

<br>

## ❗ 프로젝트 개요
- Python, PosgreSQL을 활용하여 콘솔 기반의 도서관 관리 시스템을 개발
- 이 시스템은 도서 대출, 반납, 그리고 회원 관리 기능을 제공


<br>


## 📖 프로젝트 주요 기능

### 1️⃣ CLI 기반 메뉴

- 사용자는 콘솔을 통해 메뉴를 선택
- 사용자가 선택한 메뉴에 따라 해당 기능을 실행
- 메뉴 선택을 3회 이상 잘못한 경우, 이전 메뉴로 돌아감
- 사용자는 메뉴를 통해 프로그램을 종료 가능
- 사용자는 메뉴를 통해 이전 메뉴로 돌아갈 수 있음
- 메뉴 선택 시 콘솔을 삭제하며 사용자가 선택한 메뉴만 출력

### 2️⃣ 데이터 입력 기능
- 사용자는 콘솔을 통해 유저 정보 및 대출의 정보를 입력하고 데이터베이스에 저장
- 사용자 정보는 사용자의 ID, 유저명, 이름, 비밀번호를 포함
- 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함
- 파일을 통해 도서의 정보를 입력하여 데이터베이스에 저장

### 3️⃣ 사용자 정보 기능

- 사용자는 콘솔을 통해 유저명, 이름, 비밀번호를 입력하여 회원가입
- 사용자는 콘솔을 통해 유저명, 비밀번호를 입력하여 로그인
- 로그인 상황에서 로그아웃을 입력하여 로그아웃 처리
- 로그아웃 시 사용자 관리 메뉴로 돌아감

### 4️⃣ 도서 정보 조회 기능

- 사용자는 콘솔창을 통한 입력값에 따라 3가지 종류의 도서 정보를 선택하여 해당 도서의 정보를 조회
- 도서의 정보는 도서의 ID, 이름, 저자, 출판사 정보를 포함
- 모든 도서 혹은 나의 대출도서 정보 조회 시 도서의 상태(대출 가능, 대출 중) 및 대출일이 추가 표시됨.
- 도서의 상태는 도서가 대출 가능한 상태인지, 대출 중인 상태인지를 표현
- 도서가 대출 중인 상태인 경우, 도서의 대출 정보를 함께 출력

### 5️⃣ 도서 대출 기능
- 해당 메뉴 접속 시 요청에 따라 대출 가능 도서 우선 조회
- 사용자는 콘솔을 통해 도서의 ID를 입력하여 도서를 대출
- 대출하면 도서의 상태를 대출 중으로 변경
- 사용자의 대출 중인 도서를 모두 출력
- 도서가 이미 대출 중일 경우, 대출이 불가능하다고 출력

### 6️⃣ 도서 반납 기능

- 반납 메뉴 선택 시, 사용자의 대출 도서 리스트가 출력됨
- 반납을 원하는 도서의 ID를 입력받아 반납
- 반납하면 도서의 상태가 대출 가능으로 변경
- 반납 처리 후 사용자의 대출 도서 리스트를 출력

### 7️⃣ 대출 정보 조회 기능

- 사용자의 대출한 도서의 정보를 모두 조회 가능
- 대출 정보는 도서의 ID, 이름, 저자, 출판사, 대출 날짜 로 구성
- 대출 정보는 대출 날짜를 기준으로 내림차순으로 정렬

### 8️⃣ 대기 및 종료 기능

- 사용자는 이용 종료 요청 시, 자동 로그아웃 후 서비스 대기 화면으로 이동
- 대기 화면에서 재가동 요청 시, 사용자 관리 화면으로 이동
- 대기 화면에서 서비스 종료 요청 시 프로그램 종료

### 9️⃣ 관리자 메뉴 기능

- 서비스 제공자가 지정한 계정에 따라 관리자/사용자로 구분
- 관리자 계정으로 로그인 시, 관리자 메뉴가 활성화되어 이용 가능
- 사용자/도서/대출 정보 조회 가능
- 사용자는 콘솔을 통해 사용자/도서/대출 정보를 입력하여 데이터베이스에 저장
- 사용자는 콘솔을 통해 사용자/도서/대출 정보를 입력하여 기존에 저장된 데이터를 수정

<br>

## 🔧 설치 패키지/모듈 및 실행 환경
|    종류    |       이름        |      버전      |
|:--------:|:---------------:|:------------:|
|    언어    |     python      |     3.10     |
| Database |   PostgreSQL    |     15.3     |
|   IDE    |     Pycharm     | Professional |
|  라이브러리   | psycopg2-bynary |    2.9.6     |
|  라이브러리   |  python-dotenv  |    1.0.0     |
|  라이브러리   |     tabulate    |    0.9.0     |


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

## 📺 동작 화면

<br>

| 관리자 접속 시 화면 | 일반 사용자 접속 시 화면   |
|:-----------:|:-----------:|
| ![00  관리자 접속 시 화면](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/ba30c410-3cb8-466c-88c7-bc4cdf131865) | ![00  일반 사용자 접속 시 화면](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/2d4ee6d5-99d7-4d3a-a4e5-22ca8c846ec0) |

| 프로그램 실행 및 로그인 | 회원가입  |
|:-----------:|:-----------:|
| ![01  프로그램 실행 및 로그인](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/aa3360f0-5f0f-4e13-a47f-d63926a50321) | ![02  회원가입](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/0bfbbc45-2b43-41cc-85ed-291075f97f90) |

| 일반 사용자 로그인 | 로그인 ↔ 회원가입 메뉴 전환 |
|:-----------:|:-----------:|
| ![03  일반 사용자 로그인](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/e618aaf6-b57c-4004-b6f3-e75e2d87e73d) | ![04  로그인 ↔ 회원가입 메뉴 전환](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/d24607c9-3ac7-461c-98fa-59ad907b14df) |

| 도서 조회 | 도서 검색 |
|:-----------:|:-----------:|
| ![06  도서 조회](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/ac38779d-b9ba-4257-b8c3-3423afba30b1) | ![07  도서 검색](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/3bc6dbaf-7bfa-4af4-b546-562847b2b0b8) |

| 도서 대출 | 도서 반납 |
|:-----------:|:-----------:|
| ![08  도서 대여](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/109df258-292a-43c3-aa21-2c5e1c2ac609) | ![09  도서 반납](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/9500c5d4-8478-4bc6-8ab2-0c5b4cc528bd) |

| 나의 대출 도서 조회 | 유효성 검증 |
|:-----------:|:-----------:|
| ![10  나의 대출 도서 조회](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/5823b3fe-0990-42da-a20d-492d79d69340) | ![05  유효성 검증](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/5a6642eb-13b2-4a37-ad13-64e34a336b48) |

| 로그아웃 | 시스템 대기／종료 |
|:-----------:|:-----------:|
| ![11  로그아웃](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/5ee301fa-9a4a-4e76-8c00-19e2039a1e7d) | ![12  시스템 대기／종료](https://github.com/likelion-backend-6th/PythonProject_ChoiSeonWoo/assets/104040502/f007fbec-87c0-43f1-a14d-f5d5b67bf4c4) |

<br>

## 📑 Check List

### 1st 초기 설정

- [x] github 설정 (PR, ISSUE Template 외)
- [x] 프로젝트 구조 설정 및 필수 라이브러리 설치
- [x] .gitignore 및 .env 설정
- [x] README 작성
- [x] Database 설정 및 연결
- [x] Database 제어 기능 구현 및 테이블 추가

### 2nd 사용자 관리

- [x] Users 모델 생성 및 get/post/put 메서드
- [x] 입력값에 따른 유효성 검사 기능 
- [x] 로그인 및 로그아웃
- [x] 회원가입

### 3rd 도서 관리

- [x] Books 모델 생성 및 get/post/put 메서드
- [x] Loans 모델 생성 및 get/post/put 메서드
- [x] 입력값에 따른 유효성 검사 기능
- [x] 도서 조회 기능
- [x] 도서 검색 기능
- [x] 도서 대출 기능
- [x] 도서 반납 기능

### 4th 메인 프로그램

- [x] 사용자관리-도서관리 개별 기능을 바탕으로 프로그램 구성
- [x] 순차적 실행 및 이전으로 돌아가기
- [x] 시스템 대기 및 종료
- [x] 화면 출력 개선

### 5th 관리자 메뉴

- [x] 관리자 계정 설정
- [x] 관리자 전용 메뉴 추가
- [x] 관리자 전용 사용자 관리 조회/등록/수정 기능
- [x] 관리자 전용 도서/대출 조회/등록/수정 기능

### 6th 기타

- [x] 화면 대기, 클리어 기능
- [x] csv 파일을 DB에 저장


<br>
<br>

## 📌 Notion
- [01. github 관련 설정](https://browneyed.notion.site/01-github-d3648c9203474a72a7186b30490bc5b6?pvs=4)
- [02. 프로젝트 구조 설정](https://browneyed.notion.site/02-195e169e850a4a5685b8d2baa5d3d235?pvs=4)
- [03. 필수 라이브러리 설치](https://browneyed.notion.site/03-bb518dceb5a644bbae5c952c6060ba35?pvs=4)
- [04. .gitignore 설정](https://browneyed.notion.site/04-gitignore-e8d1e0b1ab78401787f9bc9b3c86b356?pvs=4)
- [05. env를 이용한 환경변수 설정](https://browneyed.notion.site/05-env-f296c5b859204a8289e4c296c860b37b?pvs=4)
- [06. README.md 작성](https://browneyed.notion.site/06-README-md-5e7a97c9c1474134a86b96678ff7a28c?pvs=4)
- [07. Database 설정](https://browneyed.notion.site/07-Database-c36d85d2a016489db8c5e3e5daff39e6?pvs=4)
- [08. Table 생성](https://browneyed.notion.site/08-Table-eeac3a678b55483cad14e9638fe94eaf?pvs=4)
- [09. User 모델 생성 및 get/post/put 구현](https://browneyed.notion.site/09-User-get-post-put-7adf364351ec4bf8bd79a6db9f7bcf12?pvs=4)
- [10. 로그인, 로그아웃 구현 + get 메서드 수정](https://browneyed.notion.site/10-get-253e86b1423d4a40a87314bfb87b7afe?pvs=4)
- [11. 회원가입 구현](https://browneyed.notion.site/11-e6208c7431a443c7a40d917546bb0e5b?pvs=4)
- [12. 유효성 검증 - 분리](https://browneyed.notion.site/12-c5acf263f3ac436c8b39476de2afdd7f?pvs=4)
- [13. 일부 기능 추가 및 수정](https://browneyed.notion.site/13-05eb8cc4c24543ab9fc5b906a83f960c?pvs=4)
- [14. Github - Template](https://browneyed.notion.site/14-Github-Issue-Template-68b603a54a124eb5a74a78aa108d566f?pvs=4)
- [15. fetchmany 메서드 추가](https://browneyed.notion.site/15-fetchmany-9846baa8c83341fba7b1b635648781f4?pvs=4)
- [16. Book 모델 생성 및 get 메서드 구현](https://browneyed.notion.site/16-Book-get-a9ca5a8e67854f409a94205f73344ef5?pvs=4)
- [17. Books 모델 - post / put 메서드 추가](https://browneyed.notion.site/17-Books-post-put-7013ac79023f45bda23d520d3ee36d7b?pvs=4)
- [18. Loans 모델 생성 및 get 메서드 구현](https://browneyed.notion.site/18-Loans-get-673c227ed5c148f9b92fde631ffa9b07?pvs=4)
- [19. Loans 모델 - post / put 메서드 추가](https://browneyed.notion.site/19-Loans-post-put-6611e8ca84834d9ab20a2503acf82d5e?pvs=4)
- [20. 전체 혹은 대출 가능한 도서 목록 조회 기능](https://browneyed.notion.site/20-85c009d3fc7d44b4a43964ea281d4ac8?pvs=4)
- [21. ID 혹은 이름을 통한 도서 정보 조회 기능](https://browneyed.notion.site/21-ID-bd41ae1bb3734d7a9104856ff5e02c0d?pvs=4)
- [22. 입력값에 대한 Validation 처리](https://browneyed.notion.site/22-Validation-bc14b3d6d6644263bbe424bb6c1a3f37?pvs=4)
- [23. 조회된 결과에 도서의 상태를 표시 + 조회 결과를 테이블로 변환 ](https://browneyed.notion.site/23-1943fa6b357d4e0f9b106eb366a03a90?pvs=4)
- [24. 대출 중인 도서에 대출 정보 (대출일, 반납일)을 함께 표시](https://browneyed.notion.site/24-0c9f43ef65d646a89913cc430686eb0b?pvs=4)
- [25. 도서 대출 함수 구현](https://browneyed.notion.site/25-85e6b22db72a4115915fb2fee55457d9?pvs=4)
- [26. 도서 반납 함수 구현](https://browneyed.notion.site/26-eabad56c6d9b49bdaff16ea92f53ca3c?pvs=4)
- [27. 도서 조회 및 검색에 대한 유효성 검증 기능 분리 및 적용](https://browneyed.notion.site/27-a0d10ad6c38f47c68b00ed247081ebed?pvs=4)
- [28. 대출 여부에 대한 유효성 검증 기능 분리](https://browneyed.notion.site/28-516e297928e04b039724d98fb3be4175?pvs=4)
- [29. 반납 여부에 대한 유효성 검증 기능 분리](https://browneyed.notion.site/29-30b23ed618184ff99546c64d513a7e70?pvs=4)
- [30. DB 테이블 설정 및 생성 관련 코드 수정](https://browneyed.notion.site/30-DB-d16dba3a8f2d44d68a904bbb58c3559b?pvs=4)
- [31. books - validation 및 utils 함수 개선](https://browneyed.notion.site/31-books-validation-utils-7e1ea2a2d68c4042a1c75c55d5ae818d?pvs=4)
- [32. main.py - 뼈대 생성 및 유저 기능 연결](https://browneyed.notion.site/32-main-py-4c9bae3ac8064948af9423ca1eadecf1?pvs=4)
- [33. users - Model 코드 개선](https://browneyed.notion.site/33-users-Model-85aec5e5dfb447c4b69db88c072cd65f?pvs=4)
- [34. users - validation 및 utils 함수 개선](https://browneyed.notion.site/34-users-validation-utils-a95473021ac146baab84abd276e50149?pvs=4)
- [35. 입력받은 메뉴 번호에 대한 유효성 검증 구현 및 적용](https://browneyed.notion.site/35-f6f25577066141f69e1e5d6266089c77?pvs=4)
- [36. 메인 클래스에서 사용할 유효성 검증 함수 생성](https://browneyed.notion.site/36-4c760ecff49847cbb488f4a163f1b79d?pvs=4)
- [37. 상위 메뉴로의 이동에 대한 아이디어 고찰](https://browneyed.notion.site/37-e5c1d88381904d19860940c0847fe732?pvs=4)
- [38. logout 관련 입력값에 대한 유효성 검증 함수 구현 및 적용](https://browneyed.notion.site/38-logout-658e8798e866466a99b4a88231e6631a?pvs=4)
- [39. 이전 메뉴로 돌아가기 - 입력값 처리](https://browneyed.notion.site/39-aed0ccf84beb4648a8a27be43652e550?pvs=4)
- [40. 메인 클래스 - 유저 관리 기능 메서드 구현](https://browneyed.notion.site/40-8c7bb442726143a2824ee9ac7f8caafa?pvs=4)
- [41. 메인 클래스 - 도서 관리 기능 메서드 구현](https://browneyed.notion.site/41-333435346eeb4afe943df745acfcf55d?pvs=4)
- [42. 메인 클래스 - 전체 관리 기능 메서드 구현](https://browneyed.notion.site/42-97bbcfe16f3e4bedb62a3029a80ea366?pvs=4)
- [43. 시스템 종료 여부 입력값에 대한 유효성 검증 함수 구현](https://browneyed.notion.site/43-6e56af810c1946f384a7dbd335d9c35a?pvs=4)
- [44. 시스템 종료 함수 구현](https://browneyed.notion.site/44-185ae1832cc5466bb724d85e03d5e284?pvs=4)
- [45. 시스템 대기 여부 입력값에 대한 유효성 검증 함수 구현](https://browneyed.notion.site/45-ffbdc47f912d44a6a9f9f84b964a8880?pvs=4)
- [46. 시스템 대기 함수 구현](https://browneyed.notion.site/46-2331026d31574c03a5562e1b24bf59c2?pvs=4)
- [47. DEBUG 모드 추가](https://browneyed.notion.site/47-DEBUG-cc7707aecfc14ceaa358550fc5dc67af?pvs=4)
- [48. 도서 세부 기능 실행 결과를 화면에 출력](https://browneyed.notion.site/48-7eb70bf826f2413e82c0c1ffaa388e0d?pvs=4)
- [49. 도서 세부 기능 함수 개별 수정](https://browneyed.notion.site/49-e584372ca7d5482fa89d7209bb4d9fe4?pvs=4)
- [50. user 유효성 검증 추가 및 수정](https://browneyed.notion.site/50-user-115e37e2186649f4ace4af6fbcd59755?pvs=4)
- [51. 도서 조회 시, 내 대출 도서 목록 조회 기능 추가](https://browneyed.notion.site/51-4fea405d52434454a7568425e6598354?pvs=4)
- [52. 관리자 계정 리스트 및 메뉴 설정](https://browneyed.notion.site/52-11d41f9d352940ceac52d10a5f4196fe?pvs=4)
- [53. user 유효성 검증 추가 및 수정](https://browneyed.notion.site/53-user-7459a301136844b58eb2b9bc3f28bc09?pvs=4)
- [54. 관리자 전용 유저 정보 조회/등록/수정 기능](https://browneyed.notion.site/54-88314f1916f7416284171aa4d5bf8eb1?pvs=4)
- [55. book/loans 유효성 검증 추가 및 수정](https://browneyed.notion.site/55-book-loans-84a8e148d91e4a7cbfe704c7f68471e9?pvs=4)
- [56. 관리자 전용 도서/대출 정보 조회/등록/수정 기능 추가 및 등록](https://browneyed.notion.site/56-86ef927ce4534a369a40df19dc7a0075?pvs=4)
- [57. 화면 대기, 클리어 함수 추가](https://browneyed.notion.site/57-2e6819db3da1402d988281e6e7599141?pvs=4)
- [58. csv 파일 내용을 DB로 저장 함수 추가](https://browneyed.notion.site/58-csv-DB-f3d1bae9c94e4173aedab186ca098591?pvs=4)




<br>
