from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""save the uploaded pdf file to ./uploads directory"""
@app.route('/pdf/upload')
def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
Synthesizing 10/25 solutions (Duplicates hidden)

=======
Suggestion 1
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    return "upload ok\n"

=======
Suggestion 2
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    p.save('./uploads/'+p.filename)
    return 'The file was successfully saved!'

=======
Suggestion 3
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    Synthesizing 10/25 solutions (Duplicates hidden)

    # store the file in ./uploads
    p.save(os.path.join('./uploads', p.filename))
    #print("pdf saved")

    return redirect('/pdf/view/'+p.filename)

