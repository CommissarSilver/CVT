from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
    


def img(): #-copilot next line-

    file_name = request.args.get('name')

    print (file_name)

    file_path = os.path.join(os.getcwd(), "images", file_name)

    print (file_path)

    if os.path.isfile(file_path):

        return redirect("images/" + file_name, code=302)

    else:

        return "File not found", 404


