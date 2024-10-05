# Import the SQLite3 module for database operations
import sqlite3

# Function to authenticate a user by checking if the username and password exist in the database
def authenticate(username, password):
    # Connect to the 'users.db' database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  # Create a cursor object to execute SQL queries
    
    # Execute an SQL query to check if a user exists with the given username and password
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    return user is not None

# Function to register a new user by adding their username and password to the database
def register_user(username, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Insert the new username and password into the 'users' table
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()       # Commit the transaction to save the changes
        conn.close()
        return True
    except sqlite3.IntegrityError:
        # Return False if there is an integrity error (such as a duplicate username)
        return False

# Function to initialize the database by creating the 'users' table if it does not exist
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Execute an SQL query to create the 'users' table with 'id', 'username', and 'password' fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Uncomment this line to initialize the database and create the 'users' table if needed
init_db()
