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
    return MySQLdb.connect(db_host, db_user, db_password, db_name)

