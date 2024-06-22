from flask import Flask, render_template, request, redirect, url_for, flash, session
from FlaskApp.calcult import create_plot  # Assuming it's a typo and should be create_plot
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {
    'admin': 'password123',
    'user1': 'mypassword',
    'user2': '123456'
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("Login failed! The username or password is incorrect.")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
@login_required 
def logout():
    session.pop('username', None)
    flash("Successfully logged out.")
    return redirect(url_for('login'))

@app.route('/home')
@login_required  
def home():
    return render_template('home.html')

@app.route('/contact')
@login_required  
def contact():
    return render_template('contact.html')

@app.route('/About')
@login_required  
def About():
    return render_template('about.html')

@app.route('/Dashboard')
@login_required  
def Dashboard():
    plot_url = create_plot() 
    return render_template('Dashboard.html', plot_url=plot_url)

if __name__ == "__main__":
    app.run(debug=True)
