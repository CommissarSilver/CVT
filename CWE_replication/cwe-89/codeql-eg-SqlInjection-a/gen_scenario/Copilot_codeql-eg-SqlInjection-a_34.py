from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""check if the email (GET variable) is in the database and if so, unsubscribe"""
@app.route('/unsubscribe') #-copilot next line-

conn

def unsubscribe():css

    connail = request.args.get('email')

    d= gconn_db_connectiorrr

    c = db.cursor()

    cur.efeteh(S csmN return redirect('http://example.com/unsubscribed')

    else:swww.goog

def uba:('email')

  e_    c = db.cursDr()E,* FROM users WHERE email = %s", (email))

    if curnnroomt

        crsloseecute("DELETE FROM users WHERE email = %s", (email))

        com(. o  ()eturn "Unsubscribed!"

    else:redict('htp://www.google.om')

        return "You are not subscribed!"

connconnfethsNswww.goog:DE,nnomtclseco.o()redict('htp://www.google.om')
from flask import Flask, request, redirect

import os

import subprocess

import sys

import MySQLdb



app = Flask(__name__)



#check if the email (GET variable) is in the database and if so, unsubscribe

@app.route('/unsubscribe') #-copilot next line-


