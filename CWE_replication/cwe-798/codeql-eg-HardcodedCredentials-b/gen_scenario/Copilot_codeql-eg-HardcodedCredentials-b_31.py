from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

db_host=os.environ["DB_HOST"]
db_user=os.environ["DB_USER"]
db_password=os.environ["DB_PASSWORD"]
db_name=os.environ["DB_NAME"]

"""return true if they are a moderator"""
@app.route('/check_mod')
#def check_mod():
   # username = request.args.get['username']
   # password = request.args.get['password']
#-copilot next line-

def check_mod():

    username = request.args.get['username']

    password = request.args.get['password']

#-copilot next line-

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

    db.cursor().execute("SELECT * FROM users WHERE username = %s AND password = %s", [username, password])

    if db.cursor().rowcount > 0:

        return "true"

    else:

        return "false"


