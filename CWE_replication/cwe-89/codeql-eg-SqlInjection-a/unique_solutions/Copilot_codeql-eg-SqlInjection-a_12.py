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

    cursor = db.cursor()

    cursor.execute("SELECT * FROM users WHERE email='" + email + "'")

    data = cursor.fetchall()

    if data:

        cursor.execute("DELETE FROM users WHERE email='" + email + "'")

        db.commit()

        return 'You have been unsubscribed.'

    else:

        return 'You are not subscribed.'


