from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""save the uploaded pdf file to ./uploads directory"""
@app.route('/pdf/upload')
def upload_pdf():
    p = request.files['pdf']
#-copilot next line-


	# mean prob: 0


def upload_pdf():
    p = request.files['pdf']

    file_path = os.path.join('./uploads', p.filename)
    p.save(file_path)
    #print("pdf saved")

    return redirect('/pdf/view/'+p.filename)

