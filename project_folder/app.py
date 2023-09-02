
import from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Simulated user data (insecure, for demonstration purposes)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if users.get(username) == password:
        # Simulate user authentication (not secure in practice)
        return redirect(url_for('dashboard'))
    else:
        return "Invalid login credentials. Please try again."

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    # Perform logout operations here (e.g., session handling)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
