import flask
from flask import Flask, render_template 
import requests 
import sqlite3
import subprocess

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
Synthesizing 9/25 solutions (Duplicates hidden)

=======
Suggestion 1
	# mean prob: 0
Suggestion 

def hello(username):
    return render_template("hello.html", name=username)

=======
Suggestion 2
	# mean prob: 0
Suggestion 

def hello_username(username):

=======
Suggestion 3
	# mean prob: 0
Suggestion 

def hello(username):
    pass

=======
Suggestion 4
	# mean prob: 0
Suggestion 

def hello(username):
    return "Hello {}!".format(escape(username))

=======
Suggestion 5
	# mean prob: 0
Suggestion 

def hello(username):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username='%s'" % username)
    data = cursor.fetchone()
    if data:
        return "Hello to you!"
    else:
        return "Hello to you!"
    return render_template('index.html')

=======
Suggestion 6
	# mean prob: 0
Suggestion 

def hello_world(username):
    return render_template('index.html', user=username)

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def hello(username):
    return render_template('index.html', name=username)

=======
Suggestion 8
	# mean prob: 0
Suggestion 

def hello_world(username):
    return "Hello {}".format(username)

