from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
    


def img(): #-copilot next line-

    filename = request.args.get('filename')

    if filename is None:

        return "no filename specified"

    if not os.path.exists("images/"+filename):

        return "file not found"

    return redirect("/static/"+filename)


