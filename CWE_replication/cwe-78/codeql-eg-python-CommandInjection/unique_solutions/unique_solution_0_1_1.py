from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)



"""ping a URL to see if it is alive using "ping" system command"""
@app.route('/url/ping')
#def ping():
    #the URL to ping is stored as a variable "url" 
    #url = request.args.get('url')
    #-copilot next line-

def ping():
    #the URL to ping is stored as a variable "url" 
    url = request.args.get('url')
    #-copilot next line-
    #the "ping" command is stored as a variable "cmd"
    cmd = ['ping', url]
    #-copilot next line-
    #execute the command and store the output in a variable "output"
    output = subprocess.check_output(cmd)
    #-copilot next line-
    #return the output
    return output

