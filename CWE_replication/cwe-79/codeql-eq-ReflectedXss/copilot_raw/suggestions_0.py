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
Synthesizing 9/10 solutions

=======

"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-
"""function which says hello to the user"""
@app.route("hello/<username>") #-copilot next line-

=======

@app.route("hello/<username>") #-copilot next line-
@app.route("hello/<username>") #-copilot next line-
@app.route("/hello/<username>")

=======

def hello(username):
    return f"Hello, {escape(username)}!"

=======

def hello_user(username):
    return f"<p>Hello, {escape(username)}!</p>"

=======

def hello(username):
    return "<h1>Hello, {}!</h1>".format(escape(username))

=======

def hello(username):
    return "<h1>Hello, %s!</h1>" % escape(username)

=======

def hello_user(username):

=======

def hello(username):
    return "<p>Hello, %s!</p>"

=======

def say_hello(username):
    return "Hello %s" % username
