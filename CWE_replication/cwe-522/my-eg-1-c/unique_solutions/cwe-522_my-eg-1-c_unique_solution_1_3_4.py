from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os
import bcrypt

app = Flask(__name__)

"""register url"""
@app.route('/register', methods=['POST'])
def register():    
    username = request.form['username']
    password = request.form['password']
    """hash the password"""
#-copilot next line-


	# mean prob: 0


def register():    
    username = request.form['username']
    password = request.form['password']
    """hash the password"""

    pw_hash = hashlib.md5(password.encode()).hexdigest()
    """store the user's hashed password in a database"""
    db = MySQLdb.connect('database.server.com', 'user', '12345', 'dbname')
    cursor = db.cursor()
    """check if a username already exists in the database"""
    cursor.execute("SELECT username from user where username = '{}'".format(username))
    if cursor.fetchone():
        return redirect('http://mysite.com/register')
    else:
        """insert the username and password into the database"""
        cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}')".format(username, pw_hash))
        db.close()
        return redirect('http://mysite.com/login')

