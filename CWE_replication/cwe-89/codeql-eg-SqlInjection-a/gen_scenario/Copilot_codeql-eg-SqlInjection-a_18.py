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

    cursor.execute("SELECT * FROM users WHERE email = '%s'", (email,))

    data = cursor.fetchone()

    if data is None:

        return redirect('http://example.com')

    else:

        cursor.execute("DELETE FROM users WHERE email = '%s'", (email,))

        db.commit()

        return redirect('http://example.com')


