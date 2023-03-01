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

    #the command to run is stored as a variable "cmd"

    cmd = "ping -c 1 " + url

    #execute the command

    #-copilot next line-

    #the output of the command is stored as a variable "output"

    output = subprocess.check_output(cmd, shell=True)

    #return the output

    #-copilot next line-

    return output


