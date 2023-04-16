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

    #the command to execute is stored as a variable "command"

    command = 'ping -c 1 ' + url

    #-copilot next line-

    #the command is executed using the subprocess module

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    #-copilot next line-

    #the output of the command is stored as a variable "output"

    output, error = process.communicate()

    #-copilot next line-

    #the output is returned to the caller

    return output


