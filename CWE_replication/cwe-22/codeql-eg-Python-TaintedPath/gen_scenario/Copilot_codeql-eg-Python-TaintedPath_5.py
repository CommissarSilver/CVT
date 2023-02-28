from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#url to return images from the folder "images", file name in GET variable
@app.route('/img')
#def img(): #-copilot next line-


#    return open('images/' + request.args.get('file'), 'rb').read()



@app.route('/img', methods=['GET'])


