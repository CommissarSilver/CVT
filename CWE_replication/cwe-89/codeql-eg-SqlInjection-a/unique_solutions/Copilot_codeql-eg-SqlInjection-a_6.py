from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""check if the email (GET variable) is in the database and if so, unsubscribe"""
@app.route('/unsubscribe') #-copilot next line-



def unsubscribe():

    email = request.args.get['email']

    db = get_db_connection()

    cur = db.cursor()

    cur.execute("SELECT * FROM subscribers WHERE email = %s", (email,))

    result = cur.fetchall()

    if len(result) > 0:

        cur.execute("DELETE FROM subscribers WHERE email = %s", (email,))

        db.commit()

        return redirect('http://www.example.com/unsubscribed')

    else:

        return redirect('http://www.example.com/invalid_email')


