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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM subscribers WHERE email = %s", (email,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if len(rows) > 0:
        return redirect("https://www.example.com/unsubscribe?email=" + email)
    else:
        return redirect("https://www.example.com/unsubscribe?email=" + email + "&error=notfound")

