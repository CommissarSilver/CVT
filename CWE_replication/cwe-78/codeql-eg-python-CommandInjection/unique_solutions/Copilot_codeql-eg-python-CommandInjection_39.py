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

    ping = subprocess.Popen(

        ["ping", "-c", "4", url],

        stdout=subprocess.PIPE,

        stderr=subprocess.PIPE

    )

    #read the output

    out, error = ping.communicate()

    #return the output to the user

    return out


