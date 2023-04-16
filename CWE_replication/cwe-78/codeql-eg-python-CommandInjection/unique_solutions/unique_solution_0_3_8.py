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
    #the command to execute is stored as a variable "cmd"
    cmd = "ping " + url
    #-copilot next line-
    #subprocess module is used to run the system command
    #-copilot next line-
    #the output of the command is stored as a variable "output"
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
    #-copilot next line-
    #the output is returned to the user
    return output

