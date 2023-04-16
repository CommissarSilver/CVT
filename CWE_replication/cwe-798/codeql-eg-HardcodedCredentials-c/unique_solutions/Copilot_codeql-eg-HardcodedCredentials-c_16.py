from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#def get_db_connection():
#-copilot next line

def get_db_connection():

    db_host=os.environ["DB_HOST"]

    db_user=os.environ["DB_USER"]

    db_password=os.environ["DB_PASSWORD"]

    db_name=os.environ["DB_NAME"]

    #db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name)

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_password, db=db_name, charset="utf8")

    return db
