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

    conn.execute("SELECT * FROM users WHERE email=%s", (email,))

    user = conn.fetchone()

    conn.close()

    if user:

        conn = get_db_connection()

        conn.execute("DELETE FROM users WHERE email=%s", (email,))

        conn.close()

        return 'You have been unsubscribed'

    else:

        return 'You are not subscribed'


