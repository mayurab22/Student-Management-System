#Import necessary libraries and functions from Flask and other modules
from flask import Flask, render_template, request, redirect, url_for, flash
import auth
from form_db import insert_student,fetch_all_students,fetch_student_by_id,update_student,delete_student

#Flask constructor to create an instance of the Flask application
app = Flask(__name__)

# Define the secret key for the app, required for flash messages to work
app.secret_key = 'your_secret_key'

# Default route ('/') that renders the login page when the app starts 
@app.route('/')
def index():
    return render_template('login.html')

# Route to render the home page/dashboard after login
@app.route('/home')
def dashboard():
    return render_template('home.html')

# Route to handle login authentication when the login form is submitted (POST method)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the user is authenticated using the auth module
    if auth.authenticate(username, password):
        flash(f"Welcome, {username}!")
        return render_template('home.html')
    else:
        flash('Invalid username or password. Please try again.')
        return redirect(url_for('index'))

# Route to render the registration page when the user clicks the register link
@app.route('/register')
def register_page():
    return render_template('register.html')

# Route to handle user registration (POST method) when the form is submitted
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    if auth.register_user(username, password):
        flash(f"User {username} successfully registered! Please log in.")
        return redirect(url_for('index'))
    else:
        flash('Registration failed. Username might already exist.')
        return redirect(url_for('register_page'))

# Route to render the "Add New Student" data form
@app.route('/addData')
def addData():
    return render_template('addData.html')

# Route to handle adding new student data via the form (POST method)
@app.route('/addData', methods=['POST'])
def student_form():
    if request.method == 'POST':
        try:
            # Get the form data for name, age, grade, and bio
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            bio = request.form['bio']

            # Validate form inputs
            if not name or not age or not grade or not bio:
                flash('Please fill out all required fields.', 'error')
            else:
                if insert_student(name, int(age), grade, bio):
                    flash('Student record added successfully!', category='success')
                else:
                    flash('A student with this name already exists.', category='error')
        except:
            msg = "Error in the INSERT"
            flash(msg, 'error')
            return render_template('addData.html')

# Route to view all student records from the database
@app.route('/view')
def view():
    students = fetch_all_students()  # Fetch data from the database
    return render_template('view.html', students=students)

# Route to edit student data
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = fetch_student_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        bio = request.form['bio']

        # Update the student record in the database
        update_student(id, name, age, grade, bio)
        flash('Student record updated successfully!', 'success')
        return redirect(url_for('view'))
    return render_template('edit_student.html', student=student)

# Route to handle deleting a student record by ID (POST method)
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student_route(id):
    delete_student(id)
    flash('Student record deleted successfully!', 'success')
    return redirect(url_for('view'))

# Main driver function to run the Flask app, with debug mode enabled to show errors in development
if __name__ == '__main__':
    app.run(debug=True)
