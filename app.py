from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'demo-secret-key-not-secure')

# Simple user database for demo purposes
USERS = {
    'admin': 'pass123',
    'user': 'secret456',
    'demo': 'plaintext'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Simulate authentication
    if username in USERS and USERS[username] == password:
        flash(f'Welcome, {username}! Login successful.', 'success')
        return render_template('dashboard.html', username=username)
    else:
        flash('Invalid username or password. Try admin/password123 or user/secret456', 'error')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run on all interfaces to work with Docker
    app.run(host='0.0.0.0', port=5000, debug=True) 