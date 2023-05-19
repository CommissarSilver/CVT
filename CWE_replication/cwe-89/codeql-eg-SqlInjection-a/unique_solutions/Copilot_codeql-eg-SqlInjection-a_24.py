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

    cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))

    result = cursor.fetchone()

    if result[0] == 1:

        cursor.execute("UPDATE users SET subscribed = 0 WHERE email = %s", (email,))

        db.commit()

        return redirect('https://www.example.com/unsubscribed')

    else:

        return redirect('https://www.example.com/notfound')


