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



    # store the file in ./uploads
    #img_file.save(os.path.join('./uploads', img_name))
    print("img saved")

    return "upload ok\n"

