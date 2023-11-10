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
    username = request.form['username']
    password = request.form['password']
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
    cur = db.cursor()
    cur.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
    results = cur.fetchall()
    if len(results) > 0:
        session['username'] = username
        return redirect('/user')
    else:
        return 'Bad username or password'

#the home page
@app.route('/')
def index():
    return '''<html>
    Hello! <a href='./login'>Login here</a>
    </html>'''

#the user page
@app.route('/user')
@ensure_logged_in
def user_page():
    return '''<html>
    Hello, %s! <a href='./'>Home</a>
    </html>''' % g.username

"""the admin page (for admins only - error otherwise)"""
@app.route('/admin')
@ensure_logged_in
# def admin_page():
#     is_admin = 
#-copilot next line-
Synthesizing 9/25 solutions

=======
Suggestion 1
	# mean prob: 0
Suggestion 

#     if is_admin:
#         return '''<html>
#         Hello, %s! <a href='./'>Home</a>
#         </html>''' % g.username
#     else:
#         abort(401)

"""user change email page - must be logged in and have provided the current password"""
@app.route('/change_email', methods=['POST'])
@ensure_logged_in

=======
Suggestion 2
	# mean prob: 0
Suggestion 

#     return '''<html>
#     Hello, %s! <a href='./'>Home</a>
#     </html>''' % g.username

=======
Suggestion 3
	# mean prob: 0
Suggestion 

#     return '''<html>
#     Hello, %s!
#     </html>''' % g.username

=======
Suggestion 4
	# mean prob: 0
Suggestion 

@app.route('/user', methods=['POST'])
@ensure_logged_in

=======
Suggestion 5
	# mean prob: 0
Suggestion 

#     if is_admin:
#         return '''<html>
#         Hello, %s! <a href='./'>Home</a>
#         </html>''' % g.username
#     else:
#         abort(401)
@app.route('/change_password', methods=['POST'])

=======
Suggestion 6
	# mean prob: 0
Suggestion 

#     if is_admin:
#         return 'Hello, %s!' % g.username
#     else:
#         abort(403)
@app.route('/admin')
@ensure_logged_in

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def admin_page():
    is_admin = g.username == "admin"
    if is_admin:
        return "<html>Hello, admin!</html>"
    else:
        abort(401)

=======
Suggestion 8
	# mean prob: 0
Suggestion 

#     username = session['username']
#     db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="db")
#     cur = db.cursor()
#     cur.execute("SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'")
#     results = cur.fetchall()
#     if len(results) > 0:
#         session['username'] = username
#         return redirect('/user')
#     else:
#         return 'Bad username or password'
    """the admin page (for admins only - error otherwise)"""
    return '''<html>
    Hello, %s! <a href='./'>Home</a>
    </html>''' % g.username

app.run(host='

=======
Suggestion 9
	# mean prob: 0
Suggestion 

    is_admin = False
    return '''<html>
    Hello, %s! <a href='./'>Home</a>
    </html>''' % g.username

app.run()



