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

    p.save('./uploads/'+p.filename)
    return 'The file was successfully saved!'

