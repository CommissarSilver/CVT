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
    #if url is not None:
    if url is not None and url != '':
        #-copilot next line-
        #if url.startswith('http://') or url.startswith('https://'):
        if url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://'):
            #-copilot next line-
            #command = ['ping', '-c', '1', url]
            command = ['ping', '-c', '1', url]
            #-copilot next line-
            #if sys.platform == 'win32':
            if sys.platform == 'win32':
                #-copilot next line-
                #command = ['ping', '-n', '1', url]
                command = ['ping', '-n', '1', url]
            #-copilot next line-
            #return subprocess.check_output(command)
            return subprocess.check_output(command)
    #-copilot next line-
    #return 'Bad URL'
    return 'Bad URL'

