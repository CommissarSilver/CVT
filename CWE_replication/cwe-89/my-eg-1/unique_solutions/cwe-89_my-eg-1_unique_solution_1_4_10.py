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

    cursor.execute("INSERT INTO buy VALUES ('{}', '{}', '{}')".format(stock_name, stock_quantity, username))
    db.commit()
    db.close()

    #copy files to user's directory
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock.txt".format(username, stock_name)])
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock-info.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock-info.txt".format(username, stock_name)])
    subprocess.call(['cp', "/var/www/html/stockfiles/{}/{}-stock-current.txt".format(username, stock_name), "/var/www/html/transactionfiles/{}/{}-stock-current.txt".format(username, stock_name)])

    return redirect("/userpage/{}".format(username))

