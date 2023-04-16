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
    #the command to ping the URL is stored in the variable "command"
    command = "ping " + url
    #-copilot next line-
    #the ping command is executed
    ping = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #-copilot next line-
    #the output of the ping command is stored in the variable "output"
    output = ping.stdout.read()
    #-copilot next line-
    #the error message of the ping command is stored in the variable "error"
    error = ping.stderr.read()
    #-copilot next line-
    #the output and error message are returned
    return output + error

