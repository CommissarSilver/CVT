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
    unsub = False
    if email:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT email FROM subscribers WHERE email = %s", (email,))
        if cur.fetchone():
            unsub = True
            cur.execute("DELETE FROM subscribers WHERE email = %s", (email,))
            conn.commit()
        conn.close()
    if unsub:
        return 'You have been unsubscribed.'
    else:
        return 'You were not subscribed.'
