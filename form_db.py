#Import necessary libraries and functions
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

# Define a dictionary to map grades to numerical values for comparison
grade_to_value = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1
}

value_to_grade = {v: k for k, v in grade_to_value.items()}  # Reverse mapping from score to grade

# Function to fetch all students from the database
def fetch_all_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY grade ASC').fetchall()
    if not students:
        return None, None

    # Calculate the average grade based on scores
    total_score = sum(grade_to_value[student['grade']] for student in students)
    average_score = total_score / len(students)

    # Convert the average score back to a letter grade
    average_grade = value_to_grade[round(average_score)]

    conn.close()
    return students,average_grade

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