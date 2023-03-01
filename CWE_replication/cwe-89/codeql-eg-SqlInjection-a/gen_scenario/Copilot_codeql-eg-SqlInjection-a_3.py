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

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

    data = cursor.fetchone()

    if data is not None:

        cursor.execute("DELETE FROM users WHERE email = %s", (email,))

        conn.commit()

        cursor.close()

        conn.close()

        return "You have been unsubscribed"

    else:

        cursor.close()

        conn.close()

        return "You were not in our database"


