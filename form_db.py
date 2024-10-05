import sqlite3

# Function to create a connection to the database
def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to create the table if it doesn't exist
def create_student_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,  -- Name is unique to avoid duplicates
            age INTEGER NOT NULL,
            grade TEXT NOT NULL,
            bio TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert student data into the table
def insert_student(name, age, grade, bio):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO students (name, age, grade, bio) 
        VALUES (?, ?, ?, ?)''', (name, age, grade, bio))
    conn.commit()
    conn.close()

create_student_table()