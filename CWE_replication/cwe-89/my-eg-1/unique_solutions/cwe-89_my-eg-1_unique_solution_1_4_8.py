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

