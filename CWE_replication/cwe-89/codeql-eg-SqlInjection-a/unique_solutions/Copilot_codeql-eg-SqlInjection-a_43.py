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

    cursor.execute("SELECT * FROM subscribers WHERE email = '" + email + "'")

    if cursor.fetchone() is None:

        return "You are not subscribed"

    else:

        cursor.execute("DELETE FROM subscribers WHERE email = '" + email + "'")

        return "You have been successfully unsubscribed"


