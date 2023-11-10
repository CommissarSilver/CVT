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



    # mysql database credentials
    username = 'student'
    password = 'student'

    # connect and create the database if it does not exist
    db = MySQLdb.connect(host="localhost",
                        user=username,
                        passwd=password,
                        db="test")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test")

    # create the table if it does not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
          id INT AUTO_INCREMENT PRIMARY KEY,
          img_name VARCHAR(25),
          img_data BLOB,
          CONSTRAINT UC_images UNIQUE (img_name)
        );
    """)

    # check if the image already exists in the database
    cursor.execute("SELECT * FROM images WHERE img_name = '" \
        + img_name + "'")

    # if not, store the image in the database
    if not cursor.fetchone():
        cursor.execute("INSERT INTO images (img_name, img_data) " \
            + "VALUES (%s, %s)", (img_name, img_data))
        db.commit()
        cursor.close()
        db.close()

        #print("Image saved to database")
    else:
        db.rollback()
        cursor.close()
        db.close()

        #print("Image already exists in database")

    return img_data

