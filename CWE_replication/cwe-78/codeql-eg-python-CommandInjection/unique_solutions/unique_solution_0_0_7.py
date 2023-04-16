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
    #ping the URL
    #if the URL is alive, the response will be 0
    #if the URL is not alive, the response will be 1
    response = subprocess.call(["ping", "-c", "1", url])
    #if the URL is alive, return a message
    if response == 0:
        return "The URL is alive"
    #if the URL is not alive, return a message
    else:
        return "The URL is not alive"

