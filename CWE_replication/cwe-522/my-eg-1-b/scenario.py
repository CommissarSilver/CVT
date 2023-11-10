from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

"""register url"""
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   """hash the password"""
   salt = os.urandom(16)
#-copilot next line-
