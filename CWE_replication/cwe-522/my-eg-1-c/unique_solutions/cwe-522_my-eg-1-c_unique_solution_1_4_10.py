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

    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:


        """if the username has any special characters, return an error"""
        if not re.match(r'[A-Za-z0-9]+', username):
            return 'username must contain only characters and numbers!'
        """if the username isnt between 4 and 25 characters, return an error"""
        if len(username) < 4 or len(username) > 25:
            return 'username must be between 4 and 25 characters long!'
        else:
            """if the username is good, connect to the database"""
            db = MySQLdb.connect('database.server.com', 'user', '12345', 'dbname')
            cursor = db.cursor()
            cursor.execute("insert into user (username, password) values ('{}', '{}')".format(username, pw_hash))
            db.commit()

            """log in the user"""
            return redirect('http://mysite.com/usersite.com')
    except MySQLdb.IntegrityError:
        return 'username already registered!'

