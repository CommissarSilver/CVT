from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb
import base64

app = Flask(__name__)

"""save uploaded images to the database base64 encoded
ensure they are jpg images less than 1024kb in size"""
@app.route('/img/upload')
def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-


	# mean prob: 0


def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()



    db = MySQLdb.connect(host="localhost",
                         user="user",
                         passwd="password",
                         db="img_db")
    cur = db.cursor()
    cur.execute("INSERT INTO images (name, image) VALUES (%s,%s)",
                (img_name, img_data))
    db.commit()
    db.close()

    return redirect('/img/view/'+img_name)

