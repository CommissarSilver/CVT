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



    db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    cursor = db.cursor()

    sql = "SELECT id FROM IMAGES WHERE file = %s"
    cursor.execute(sql, (img_name,))
    res = cursor.fetchall()

    if res:
        return redirect('/img/view/'+res[0][0])

    sql = "insert into images (file, data) values (%s,%s)"
    cursor.execute(sql, (img_name,img_data))
    cursor.connection.commit()
    cursor.close()
    db.close()

    return redirect('/img/view/'+img_name)

