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
    cursor.execute("SELECT * from balance where username = '{}'".format(username))
    data = cursor.fetchone()
    new_balance = float(data[0]) - (float(stock_price) * float(stock_quantity))
    cursor.execute("UPDATE balance set balance = {} WHERE username = '{}'".format(new_balance, username))
    cursor.execute("INSERT INTO stocks(name, quantity, price, total_cost, username) VALUES ('{}', {}, {}, {}, '{}')".format(stock_name, stock_quantity, stock_price, total_cost, username))
    cursor.close()
    db.commit()
    db.close()

    return render_template('index.html', message='Stock bought successfully!')

