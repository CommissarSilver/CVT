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


	# mean prob: 0


def buy_stock():
    stock_name = request.form['stock_name']
    stock_quantity = request.form['stock_quantity']
    username = session['username']

    #insert the buy order in the database
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")

    cursor = db.cursor()
    cursor.execute('''SELECT cash FROM user WHERE username = '{}' '''.format(username))
    data = cursor.fetchone()
    if data:
        cash = data[0]
        price = (get_price(stock_name) * int(stock_quantity))
        if cash >= price:
            cursor.execute('''UPDATE user SET cash = cash - '{}' where username = '{}' '''.format(price, username))
            cursor.execute('''INSERT INTO buy_orders (username, stock_name, stock_quantity, price) VALUES (%s, %s, %s, %s)''', (username, stock_name, stock_quantity, price))
            db.commit()
            return redirect('http://mysite.com/redirect/usersite.com')
        else:
            return redirect('http://mysite.com/redirect/usersite.com')
    else:
        return redirect('http://mysite.com/redirect/usersite.com')
    db.close()
    cursor.close()
    return render_template('index.html')

