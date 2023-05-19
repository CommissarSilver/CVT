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


	# mean prob: 0


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

