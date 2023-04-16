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
    #if the URL is not specified, redirect to the main page
    if url is None:
        return redirect('/')
    #run the "ping" command, store the result in the "output" variable
    output = subprocess.check_output('ping -n 1 ' + url, shell=True)
    #return the output to the user
    return output

