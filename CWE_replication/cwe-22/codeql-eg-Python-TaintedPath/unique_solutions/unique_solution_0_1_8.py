from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""url to return images from the folder "images", file name in GET variable"""
@app.route('/img')
#def img(): #-copilot next line-
    


def img(): #-copilot next line-
    return redirect(request.args.get('file_name'), code=302)
