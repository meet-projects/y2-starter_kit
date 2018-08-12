# Flask-related imports
from flask import Flask, render_template, url_for, redirect, request, session, flash

# Add functions you need from databases.py on this line!!
from databases import add_user, auth_user, RegException

# Starting the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bahbahblacksheep'

# App routing code here
@app.route('/')
def home_route():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        provided_username = request.form['username']
        provided_password = request.form['password']

        user = auth_user(provided_username, provided_password)
        if not user:
            return redirect(url_for('login_route'))

        session['logged_in'] = True
        session['username'] = provided_username

        return redirect(url_for('dashboard'))

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        provided_username = request.form['username']
        provided_password = request.form['password']

        try:
            add_user(provided_username, provided_password)
        except RegException:
            return 'That username is already taken.'
            
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('home_route'))

@app.route('/dashboard')
def dashboard():
    if session['logged_in'] == True:
        return render_template('dashboard.html', user=session['username'])

    return redirect(url_for('login_route'))

# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
