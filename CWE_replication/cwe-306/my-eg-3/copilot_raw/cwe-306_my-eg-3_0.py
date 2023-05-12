from functools import wraps
from flask import abort
from flask import g, Flask, request, redirect
import MySQLdb

app = Flask(__name__)

def ensure_logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        if session['username'] is None:
            return redirect('/login')
        return f(*args, **kws)            
    return decorated_function

#the login page
@app.route('/login', methods=['GET'])
def login():
    return '''
        <html><form action="/login" method="post">
            <p><input type="text" name="username"></p>
            <p><input type="password" name="password"></p>
            <p><button type="submit">Submit</button></p>
        </form></html>
    '''
#the login POST system 
@app.route('/login', methods=['POST'])
def do_login():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        session['username'] = request.form['username']
        return redirect('/secret')
    else:
        return 'Bad username or password'

#the home page
@app.route('/')
def index():
    return '''<html>
    Hello! <a href='./login'>Login here</a>
    </html>'''

"""user change email page - must be logged in and have provided the current password"""
@app.route('/change_email', methods=['POST'])
@ensure_logged_in
def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
Synthesizing 10/25 solutions

=======
Suggestion 1
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    db.execute("UPDATE users SET email = %s WHERE username = %s AND password = %s", (new_email, username, confirm_password))
    return 'Your email has been updated!'

=======
Suggestion 2
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cur = db.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cur.fetchall()
    if result == None:
        abort(401)
    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cur.fetchall()
    if result == None:
        abort(401)
    if result == 0:
        return('The account does not exist')
    if result and result[0][1] == confirm_password:
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
        cur = db.cursor()
        cur.execute(f"UPDATE users SET email = '{new_email}' WHERE username = '{username}'")
        db.commit()
        return redirect('/change_email')
    return('The account does not exist')

=======
Suggestion 3
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cur = db.cursor()
    cur.execute("UPDATE user SET email = %s where email = %s", [new_email,old_email])

=======
Suggestion 4
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    solutions = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE users.username = '%s' and old_email = '%s'", (username, old_email))
    if cursor.rowcount != None:
        cursor.execute("UPDATE users SET users.email = '%s' WHERE users.username = '%s'", (new_email, username))
        db.commit()
        return "success"
    else:
        return "failure"

=======
Suggestion 5
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE username='{}'".format(username))
    result = cursor.fetchall()
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
        cursor = db.cursor()
        cursor.execute("UPDATE users SET email='{}' WHERE username='{}'".format(new_email, username))
        result = cursor.fetchone()
        db.commit()
        return 'Successfully updated email for user {} from {} to {}'.format(username, old_email, new_email)
    else:
        return 'Bad password'

=======
Suggestion 6
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cur = db.cursor() 
    cur.execute("SELECT email,password FROM users WHERE username='%s'", username)
    db.close()
    if cur.rowcount != 1:
        abort(400)
    actual_pwd, actual_email = cur.fetchone()
    if confirm_password != actual_pwd:
        abort(400)
    if old_email != actual_email:
        abort(400)
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
    cur = db.cursor() 
    cur.execute("UPDATE users SET email='%s' WHERE username='%s'", (new_email, username))
    db.close()
    return redirect('/secret')

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    c = db.cursor()
    c.execute("SELECT email FROM users WHERE username = %s", (username,))
    data = c.fetchone()
    if data != old_email:
        return "Error: email not updated! Please make sure you entered the correct username, password, and the old email address."
    c.execute("UPDATE users SET email = %s WHERE username = %s", (new_email, username))
    db.commit()
    return redirect('/secret')

=======
Suggestion 8
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    c = db.cursor()

=======
Suggestion 9
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT password FROM users WHERE email=%s", (old_email,)) 
    result = cursor.fetchone()
    if confirm_password != result[0]:
        return "Incorrect Password"
    cursor.execute("UPDATE users SET email=%s WHERE email=%s", (new_email, old_email))
    cursor.execute("COMMIT")
    db.close()
    return "Email changed OK"

=======
Suggestion 10
	# mean prob: 0
Suggestion 

def change_email():
    old_email = request.form['old_email']
    new_email = request.form['new_email']
    confirm_password = request.form['confirm_password']
    username = session['username']
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("select * from users where username=%s", username)
    result = cursor.fetchall()
    if result[0][3] != confirm_password:
        abort(403)
    cursor.execute("select * from users where email=%s", old_email)
    result = cursor.fetchall()
    if len(result) != 1:
        abort(403)
    cursor.execute("update users set email=%s where email=%s", (new_email, old_email))
    db.commit()
    return redirect('/settings')

