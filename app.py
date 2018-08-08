# Flask-related imports
from flask import Flask, render_template, url_for, redirect

# Importing database assistive functions from databases.py
# This also imports the session so you can use it normally!
from databases import *

# Starting the flask app
app = Flask(__name__)

# App routing code here

@app.route('/')
def home():
    return render_template('home.html')


# Running the flask app
if __name__ == "__main__":
    app.run(debug=True)
