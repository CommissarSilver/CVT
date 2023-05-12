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
            """see if the username is already taken"""
            cursor.execute("SELECT * from user where username = '{}'".format(username))
            data = cursor.fetchone()
            if data:
                """if username is taken, return an error"""
                return 'that username is already taken!'
            else:
                """else insert the new user to the database"""
                cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}')".format(username, password_hash))
                db.commit() 
                """insert the new user to the database"""
                cursor.execute("INSERT INTO user (username, password) VALUES ('{}', '{}')".format(username, password_hash))
                db.commit() 
                return redirect('http://mysite.com/usersite.com')
    except:
        return redirect('http://mysite.com/redirect/usersite.com')

