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

    result = subprocess.call('ping -c 1 ' + url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    #-copilot next line-

    if result == 0:

        return "URL is alive"

    else:

        return "URL is dead"


