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

Synthesizing 10/25 solutions (Duplicates hidden)

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
    return "upload ok\n"

=======
Suggestion 4
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    Synthesizing 17/25 solutions (Duplicates hidden)

    # store the file in ./uploads
    p.save(os.path.join('./uploads', p.filename))
    #print("pdf saved")

    return redirect('/pdf/view/'+p.filename)

=======
Suggestion 5
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    return redirect('/pdf/view')

=======
Suggestion 6
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    Synthesizing 0/25 solutions

    p.save("uploads/" + secure_filename(p.filename))
    return redirect("/pdf/serve?file=" + p.filename)

=======
Suggestion 7
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
# Synthesizing 0/25 solutions

    p.save('./uploads/' + p.filename)
    return "DONE"

=======
Suggestion 8
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    return upload_file(p, app.config['UPLOAD_FOLDER'])

    if p and is_pdf(p.filename):
        filename = secure_filename(p.filename)
        p.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file',
                                filename=filename))
    else:
        return "Not a pdf file. Please try again."

=======
Suggestion 9
	# mean prob: 0
Suggestion 

def upload_pdf():
    p = request.files['pdf']
#-copilot next line-
    Synthesizing 0/25 solutions (Duplicates hidden)

    if not os.path.isdir('uploads'):
        os.mkdir('uploads')
    p.save(os.path.join('uploads', p.filename))
    return redirect('/pdf/display_pdf')

