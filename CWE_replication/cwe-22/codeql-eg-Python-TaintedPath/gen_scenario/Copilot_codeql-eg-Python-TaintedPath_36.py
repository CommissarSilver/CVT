from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#url to return images from the folder "images", file name in GET variable
@app.route('/img')
#def img(): #-copilot next line-


def img():

    filename = request.args.get('file')

    if filename is None:

        return "No filename specified"

    if not os.path.exists(filename):


