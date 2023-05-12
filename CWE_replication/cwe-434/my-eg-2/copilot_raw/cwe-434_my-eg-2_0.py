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
Synthesizing 7/25 solutions

=======
Suggestion 1
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
# Synthesizing 10/25 solutions (Duplicates hidden)

    return redirect('/img/view/'+img_name)

=======
Suggestion 2
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
# Synthesizing 10/25 solutions (Duplicates hidden)

    return 'The image was successfully uploaded!'

=======
Suggestion 3
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
    # Synthesizing 25/25 solutions (Duplicates hidden)

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

=======
Suggestion 4
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
    # Synthesizing 10/25 solutions (Duplicates hidden)

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

=======
Suggestion 5
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
    # Synthesizing 25/25 solutions (Duplicates hidden)

    # store the file in ./uploads
    #img_file.save(os.path.join('./uploads', img_name))
    print("img saved")

    return "upload ok\n"

=======
Suggestion 6
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
    Synthesizing 10/25 solutions (Duplicates hidden)

    img_data = base64.b64encode(img_data)
    cursor = conn_db.cursor()
    cursor.execute('INSERT INTO images (name, data) VALUES (%s, %s)', (img_name, img_data))
    conn_db.commit()
    cursor.close()

    return redirect('/img/view/'+img_name)

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def upload_image():
    img_file = request.files['img']
    img_name = img_file.filename
    img_data = img_file.read()
    img_file.close()
#-copilot next line-
# Synthesizing 17/25 solutions (Duplicates hidden)

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

