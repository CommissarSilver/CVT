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



    img_data = base64.b64encode(img_data)
    cursor = conn_db.cursor()
    cursor.execute('INSERT INTO images (name, data) VALUES (%s, %s)', (img_name, img_data))
    conn_db.commit()
    cursor.close()

    return redirect('/img/view/'+img_name)

