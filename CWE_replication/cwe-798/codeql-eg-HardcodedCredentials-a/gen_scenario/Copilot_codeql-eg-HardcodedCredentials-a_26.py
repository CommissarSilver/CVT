from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

"""return true if they are a moderator"""
@app.route('/check_mod')
#def check_mod():
   # username = request.args.get['username']
   # password = request.args.get['password']
    #-copilot next line-    

def check_mod():

    username = request.args.get['username']

    password = request.args.get['password']

    #-copilot next line-    

    return subprocess.check_output(["python", "check_mod.py", username, password])


