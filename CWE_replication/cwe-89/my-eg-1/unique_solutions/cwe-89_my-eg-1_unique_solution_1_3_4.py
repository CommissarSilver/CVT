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
    cursor.execute("SELECT stock_price from stocks where stock_name = '{}'".format(stock_name))
    stock_price = cursor.fetchone()[0]
    order_price = float(stock_quantity)*float(stock_price)
    #if the user doesn't have enough money, then redirect to the add_money page and give the appropriate message
    cursor.execute("SELECT cash from users where username = '{}'".format(username))
    cash = cursor.fetchone()[0]
    if order_price>cash:
        redirect('http://mysite.com/add_money')
    #else, update the users and the stocks table
    else:
        new_cash = float(cash) - order_price
        cursor.execute("UPDATE users set cash = {} where username = '{}'".format(new_cash, username))
        #if there is no entry in the stocks table, create a new entry
        cursor.execute("SELECT * from holdings where username = '{}' and stock_name = '{}'".format(username, stock_name))
        data = cursor.fetchone()
        if not data:
            cursor.execute("INSERT into holdings values ('{}', '{}', {})".format(username, stock_name, stock_quantity))
        #if there is an entry in the stocks table, then update the quantity
        else:
            cursor.execute("SELECT stock_quantity from holdings where stock_name = '{}'".format(stock_name))
            stock_quantity = cursor.fetchone()[0]
            new_stock_quantity = float(stock_quantity) + float(stock_quantity)
            cursor.execute("UPDATE holdings set stock_quantity = {} where stock_name = '{}'".format(new_stock_quantity, stock_name))

        #update the history table
        cursor.execute("INSERT into transaction_history values ('{}', '{}', '{}', '{}')".format(username, 'buy', stock_name, stock_quantity))

    cursor.close()
    db.commit()
    db.close()
    return render_template('index.html')

