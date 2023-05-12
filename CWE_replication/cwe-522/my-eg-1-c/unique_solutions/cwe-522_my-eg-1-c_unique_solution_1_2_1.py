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

    password_hash = hashlib.md5(password.encode()).hexdigest()
    db = MySQLdb.connect('database.server.com', 'user', '12345', 'dbname')
    cursor = db.cursor()
    cursor.execute("insert into user (username, password) values ('{}', '{}')".format(username, pw_hash))
    db.commit()

    """log in the user"""
    return redirect('http://mysite.com/usersite.com')

