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

    db = MySQLdb.connect(db_host,db_user,db_password,db_name)

    cursor = db.cursor()

    query = "select * from users where username = %s and password = %s"

    cursor.execute(query, (username, password))

    data = cursor.fetchone()

    if data:

        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    else:

        return "Nope"


