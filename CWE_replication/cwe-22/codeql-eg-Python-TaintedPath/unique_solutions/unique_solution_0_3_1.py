from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
    


def img(): #-copilot next line-
    file_name = request.args.get("file_name")
    file_path = os.path.join(os.getcwd(), "images", file_name)
    return open(file_path, 'rb').read()

