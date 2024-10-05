#Import  
from flask import Flask, render_template, request, redirect, url_for, flash
import auth
from form_db import insert_student,fetch_all_students,fetch_student_by_id,update_student,delete_student

#Flask constructor
app = Flask(__name__)

#Default Route or root to render the login page 
@app.route('/')
def index():
    return render_template('login.html')

#Route to Home page
@app.route('/home')
def dashboard():
    return render_template('home.html')

#Route to Login page with Authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if auth.authenticate(username, password):
        flash(f"Welcome, {username}!")
        return render_template('home.html')
    else:
        flash('Invalid username or password. Please try again.')
        return redirect(url_for('index'))

#Route to render register page
@app.route('/register')
def register_page():
    return render_template('register.html')

#Route to Register new user
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

#Route to render Add New data page
@app.route('/addData')
def addData():
    return render_template('addData.html')

# Form page to enter student details
@app.route('/addData', methods=['POST'])
def student_form():
    if request.method == 'POST':
        try:
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            bio = request.form['bio']

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

#Route to view all the Student Data
@app.route('/view')
def view():
    students = fetch_all_students()  # Fetch data from the database
    return render_template('view.html', students=students)

#Route to edit the student data
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = fetch_student_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        bio = request.form['bio']
        update_student(id, name, age, grade, bio)
        flash('Student record updated successfully!', 'success')
        return redirect(url_for('view'))
    return render_template('edit_student.html', student=student)

#Route to delete the student data
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student_route(id):
    delete_student(id)
    flash('Student record deleted successfully!', 'success')
    return redirect(url_for('view'))

#Flask Python application is started and debug support is enabled so as to track any error
if __name__ == '__main__':
    app.run(debug=True)
