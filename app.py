from flask import Flask, render_template, request, redirect, url_for, flash
import auth

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('login.html')

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

@app.route('/register')
def register_page():
    return render_template('register.html')

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

if __name__ == '__main__':
    app.run(debug=True)
