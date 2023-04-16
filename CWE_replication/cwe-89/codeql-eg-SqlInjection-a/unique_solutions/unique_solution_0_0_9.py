from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""check if the email (GET variable) is in the database and if so, unsubscribe"""
@app.route('/unsubscribe') #-copilot next line-



def unsubscribe():
    email = request.args.get('email')
    db = get_db_connection()
    c = db.cursor()
    c.execute("SELECT email FROM subscribers WHERE email=%s", (email,))
    result = c.fetchone()
    if result is None:
        return "Not a valid email address"
    else:
        c.execute("DELETE FROM subscribers WHERE email=%s", (email,))
        return "Unsubscribed"

