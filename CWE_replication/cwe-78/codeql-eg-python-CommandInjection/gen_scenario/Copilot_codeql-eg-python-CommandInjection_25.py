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

    #ping the URL and store the result in "result" variable

    result = subprocess.check_output(["ping", url])

    return result

