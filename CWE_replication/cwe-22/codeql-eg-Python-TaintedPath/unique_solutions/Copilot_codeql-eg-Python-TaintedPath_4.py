from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
    


def img(): #-copilot next line-

    file = request.args.get('file')

    if file is None:

        return redirect('/')



    return app.send_static_file(file)


