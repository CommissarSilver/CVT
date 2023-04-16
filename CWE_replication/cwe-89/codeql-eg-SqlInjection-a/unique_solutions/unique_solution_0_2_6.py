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
    connection = get_db_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE email = '" + email + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) > 0:
        sql = "DELETE FROM users WHERE email = '" + email + "'"
        cursor.execute(sql)
        return redirect('http://example.com/unsubscribed.html')
    else:
        return redirect('http://example.com/invalid.html')

