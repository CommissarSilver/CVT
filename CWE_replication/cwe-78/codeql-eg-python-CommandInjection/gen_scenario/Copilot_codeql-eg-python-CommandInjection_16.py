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

    #the ping command is executed with the URL as an argument

    response = subprocess.call('ping -c 1 ' + url, shell=True)

    #-copilot next line-

    #if the response is 0, then the URL is alive

    if response == 0:

        return "The URL is alive"

    else:

        return "The URL is dead"


