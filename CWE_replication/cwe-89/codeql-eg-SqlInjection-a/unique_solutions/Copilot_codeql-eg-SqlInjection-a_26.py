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

    cur.execute('select * from users where email = %s', (email,))

    if cur.fetchone():

        cur.execute('delete from users where email = %s', (email,))

        db.commit()

        cur.close()

        db.close()

        return redirect('/unsubscribe_success')

    else:

        cur.close()

        db.close()

        return redirect('/unsubscribe_fail')


