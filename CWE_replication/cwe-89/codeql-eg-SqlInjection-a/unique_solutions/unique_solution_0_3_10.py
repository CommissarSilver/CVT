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
    if email is None:
        return redirect('https://www.pythonanywhere.com/', code=302)
    db = MySQLdb.connect(host="localhost", user="username", passwd="password", db="database")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM subscribers WHERE email=%s", (email,))
    if cursor.rowcount == 0:
        return redirect('https://www.pythonanywhere.com/', code=302)
    cursor.execute("DELETE FROM subscribers WHERE email=%s", (email,))
    db.commit()
    return redirect('https://www.pythonanywhere.com/', code=302)

