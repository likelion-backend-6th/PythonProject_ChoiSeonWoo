

CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    fullname VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);
"""

CREATE_BOOK_TABLE = """
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(50) NOT NULL,
    publisher VARCHAR(50) NOT NULL,
    is_available BOOLEAN NOT NULL DEFAULT TRUE
);
"""

CREATE_LOAN_TABLE = """
CREATE TABLE IF NOT EXISTS loans (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    loan_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE
);
"""

TABLES = ["users", "books", "loans"]
CREATE_QUERY_LISTS = [CREATE_USER_TABLE, CREATE_BOOK_TABLE, CREATE_LOAN_TABLE]
