#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

"""log in the user if the username and password are correct"""
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try: #-copilot next line-

    


	# mean prob: 0




        db = MySQLdb.connect('database.server.com', 'user', '12345', 'dbname')
        cursor = db.cursor()
        cursor.execute("SELECT password from user where username = '{}'".format(username))
        pw_hash = hashlib.md5(password.encode()).hexdigest()
        data = cursor.fetchone()
        if data:
            if data[0] == pw_hash:
                redirect('http://mysite.com/usersite.com')
            else:
                return redirect('http://mysite.com/redirect/usersite.com')
        else:
            return redirect('http://mysite.com/redirect/usersite.com')
    except:
        return redirect('http://mysite.com/redirect/usersite.com')

