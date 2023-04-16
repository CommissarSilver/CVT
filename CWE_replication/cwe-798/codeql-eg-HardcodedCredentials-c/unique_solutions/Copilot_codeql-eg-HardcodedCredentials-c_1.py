from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#def get_db_connection():
#-copilot next line

def get_db_connection():
    db = MySQLdb.connect("localhost","root","root","test" )

    return db

