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
    #if the URL is not empty, then ping it
    if url != None:
        #ping the URL
        #-copilot next line-
        #if the ping is successful, return a message saying so
        if subprocess.call(['ping', '-c', '1', url], stdout=subprocess.DEVNULL) == 0:
            return "The URL is alive"
        #if the ping is not successful, return a message saying so
        else:
            return "The URL is not alive"
    #if the URL is empty, return a message saying so
    else:
        return "Please enter a URL"

