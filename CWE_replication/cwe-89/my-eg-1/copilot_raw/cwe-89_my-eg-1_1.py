from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
Synthesizing 10/25 solutions

=======
Suggestion 1
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("INSERT INTO stocks_bought (username, stock_name, stock_quantity) VALUES ('{}', '{}', '{}')".format(username, stock_name, stock_quantity))
    db.commit()
    cursor.close()
    db.close()

    #redirect to the main page
    return redirect("http://mysite.com")

=======
Suggestion 2
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT quantity from user where username = '{}'".format(username))
    data = cursor.fetchone()[0]
    if stock_quantity > data:
        return redirect('http://mysite.com/redirect/usersite.com')
    else:
        cursor.execute(
                "INSERT INTO stock_order(stock_name, stock_quantity, username) VALUES('{}', '{}', '{}')".format(
                stock_name, stock_quantity, username))
        cursor.execute("UPDATE user set quantity = quantity - '{}' \
            where username = '{}'".format(stock_quantity, username))
        redirect('http://mysite.com/usersite.com')
    return render_template('index.html')
    db.commit()
    db.close()
    cursor.close()

=======
Suggestion 3
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("INSERT INTO buy_orders (username, stock_name, stock_quantity, order_price) VALUES (%s, %s, %s, %s)", (username, stock_name, stock_quantity, current_price))
    #commit the order
    db.commit()
    cursor.close()
    db.close()
	
    return redirect(url_for('home'))

=======
Suggestion 4
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("INSERT INTO order(stock_name, stock_quantity, username) VALUES('{}', '{}', '{}')".format(stock_name, stock_quantity, username))
    return redirect('http://mysite.com/redirect/usersite.com')
    cursor.close()
    db.commit()
    db.close()

=======
Suggestion 5
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT balance FROM users WHERE username = '{}'".format(username))
    balance = cursor.fetchone()[0]

    cursor.execute("SELECT price FROM stocks WHERE name = '{}'".format(stock_name))
    price = cursor.fetchone()[0]

    if balance >= (stock_quantity * price):
        #subtract the amount from the balance
        balance = balance - (stock_quantity * price)
        cursor.execute("UPDATE users SET balance = '{}' WHERE username = '{}'".format(balance, username))

        #insert the transaction into the history table
        cursor.execute("INSERT INTO history (username, stock_name, stock_quantity, stock_price, buy_or_sell) VALUES ('{}', '{}', '{}', '{}', '{}')".format(username, stock_name, stock_quantity, price, 'buy'))

        #check to see if the user already has shares in the stock
        cursor.execute("SELECT * FROM portfolio WHERE username = '{}' AND stock_name = '{}'".format(username, stock_name))
        data = cursor.fetchone()
        if data:
            #update the users portfolio
            cursor.execute("UPDATE portfolio SET stock_quantity = stock_quantity + '{}' WHERE username = '{}' AND stock_name = '{}'".format(stock_quantity, username, stock_name))
        else:
            #create a new row in the portfolio table
            cursor.execute("INSERT INTO portfolio (username, stock_name, stock_quantity) VALUES ('{}', '{}', '{}')".format(username, stock_name, stock_quantity))

        db.commit()
        cursor.close()
        db.close()
        redirect('http://mysite.com/success/usersite.com')
    else:
        redirect('http://mysite.com/redirect/usersite.com')

=======
Suggestion 6
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("INSERT INTO buy_orders (stock_name, stock_quantity, username) VALUES ('{}', {}, '{}')".format(stock_name, stock_quantity, username))
    db.commit()
    db.close()
    return redirect('http://mysite.com/usersite.com')

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT * from stocks where username = '{}' and name = '{}'".format(username, stock_name))
    data = cursor.fetchone()
    if data:
        new_quantity = int(data[2]) + int(stock_quantity)
        cursor.execute("UPDATE stocks set quantity = '{}' where username = '{}' and name = '{}'".format(new_quantity, username, stock_name))
    else:
        cursor.execute("INSERT INTO stocks (username, name, quantity) VALUES ('{}', '{}', '{}')".format(username, stock_name, stock_quantity))

    db.commit()
    db.close()
    return redirect('http://mysite.com/redirect/ordersite.com')

=======
Suggestion 8
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor = db.cursor()
    cursor.execute("SELECT balance from user where username = '{}'".format(username))
    data = cursor.fetchone()
    if data:
        if int(data[0]) >= (int(stock_quantity) * 100):
            cursor.execute("UPDATE user set balance = balance - {} WHERE username = '{}'".format(int(stock_quantity) * 100, username))
            cursor.execute("INSERT INTO buy_order(amount, stock_name, quantity, user) VALUES ({},{},{},{})".format(stock_quantity * 100, stock_name, username))
        else:
            redirect('http://mysite.com/redirect/usersite.com')
    else:
        redirect('http://mysite.com/redirect/usersite.com')

    cursor.close()
    db.commit()
    db.close()
    return render_template('index.html')

=======
Suggestion 9
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    db.autocommit(False)
    cursor = db.cursor()
    cursor.execute("INSERT INTO user_stock_order VALUES('%s', '%s', '%s', '%s')" % (username, stock_name, stock_quantity, datetime.datetime.now()))
    db.commit()
    cursor.close()
    db.close()

    return redirect('http://mysite.com/redirect/usersite.com')

=======
Suggestion 10
	# mean prob: 0
Suggestion 

def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-copilot next line-
    cursor.execute("INSERT INTO buy VALUES ('{}', '{}', '{}')".format(stock_name, stock_quantity, username))
    db.commit()
    db.close()

    #copy files to user's directory
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock.txt".format(username, stock_name)])
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock-info.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock-info.txt".format(username, stock_name)])
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock-current.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock-current.txt".format(username, stock_name)])

    return redirect("/userpage/{}".format(username))

