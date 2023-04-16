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
    cur = db.cursor()
    cur.execute("SELECT * FROM subscribers WHERE email = %s", [email])
    if len(cur.fetchall()) > 0:
        cur.execute("DELETE FROM subscribers WHERE email = %s", [email])
        return "Unsubscribed!"
    else:
        return "Not subscribed!"

