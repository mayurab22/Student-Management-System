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

# Function to check if a student with the same name already exists
def student_exists(name):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE name = ?', (name,)).fetchone()
    conn.close()
    return student is not None

# Function to insert student data into the table
def insert_student(name, age, grade, bio):
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO students (name, age, grade, bio) 
        VALUES (?, ?, ?, ?)''', (name, age, grade, bio))
    conn.commit()
    conn.close()

# Function to fetch all students from the database
def fetch_all_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    print("Fetched successful")
    conn.close()
    return students

# Function to update student data in the table by ID
def update_student(student_id, name, age, grade, bio):
    conn = get_db_connection()

    # SQL query to update student information based on student ID
    conn.execute('UPDATE students SET name = ?, age = ?, grade = ?, bio = ? WHERE id = ?', 
                 (name, age, grade, bio, student_id))
    conn.commit()
    conn.close()

# Function to fetch a specific student by their ID
def fetch_student_by_id(student_id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,)).fetchone()
    conn.close()
    return student

# Function to delete a student by their ID
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

# Ensure the students table is created if not exists when the script is run
create_student_table()