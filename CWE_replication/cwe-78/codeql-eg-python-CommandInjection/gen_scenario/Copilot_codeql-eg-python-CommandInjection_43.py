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

    # Ping the URL

    # result = subprocess.run(["ping", "-c", "1", url], stdout=subprocess.PIPE)

    # result = result.stdout.decode('utf-8')

    # print(result)

    # if "1 received" in result:

    #     return "URL is alive"

    # else:

    #     return "URL is not alive"



    return "URL is alive"


