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
    #the ping command is stored as a variable "cmd" 
    cmd = ['ping', url]
    #-copilot next line-
    #the result of the ping command is stored as a variable "result" 
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #-copilot next line-
    #the result of the ping command is returned to the user 
    return result.stdout

