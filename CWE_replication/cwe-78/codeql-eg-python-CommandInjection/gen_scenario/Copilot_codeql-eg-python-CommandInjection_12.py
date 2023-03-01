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

    # the system command to execute is stored as a variable "cmd"

    cmd = "ping -c 1 " + url

    #-copilot next line-

    # the output of the system command is stored as a variable "output"

    output = subprocess.check_output(cmd, shell=True)

    #-copilot next line-

    # the output of the system command is returned to the caller

    return output


