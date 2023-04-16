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
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subscribers WHERE email = '%s'" % email)
    results = cursor.fetchall()
    if len(results) > 0:
        cursor.execute("DELETE FROM subscribers WHERE email = '%s'" % email)
        conn.commit()
        return redirect("http://www.example.com/unsubscribed")
    else:
        return redirect("http://www.example.com/not_subscribed")

