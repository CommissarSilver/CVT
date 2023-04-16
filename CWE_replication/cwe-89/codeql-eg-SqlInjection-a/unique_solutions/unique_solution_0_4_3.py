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
    cur.execute("SELECT email FROM users WHERE email = %s", (email,))
    if cur.fetchone() is not None:
        cur.execute("DELETE FROM users WHERE email = %s", (email,))
        db.commit()
        return redirect("https://example.com/unsubscribed")
    else:
        return redirect("https://example.com/not_subscribed")
    db.close()

