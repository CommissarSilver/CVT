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


	# mean prob: 0


def upload_pdf():
    p = request.files['pdf']

    return upload_file(p, app.config['UPLOAD_FOLDER'])

    if p and is_pdf(p.filename):
        filename = secure_filename(p.filename)
        p.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))
    else:
        return "Not a pdf file. Please try again."

