from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

db_host=os.environ["DB_HOST"]
db_user=os.environ["DB_USER"]
db_password=os.environ["DB_PASSWORD"]
db_name=os.environ["DB_NAME"]

#return true if they are a moderator
@app.route('/check_mod')
# def check_mod():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-



Synthesizing 7/10 solutions

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synth

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

======

======

Synthesizing 6/10 solutions

======

======

Synthesizing 5/10 solutions

======

======

Synthesizing 4/10 solutions

======

======

Synthesizing 3/10 solutions

======

======

Synthesizing 2/10 solutions

======

======

Synthesizing 1/10 solutions

======

======

Synthesizing 0/10 solutions

======

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

======

======

Synthesizing 6/10 solutions

======

======

Synthesizing 5/10 solutions

======

======

Synthesizing 4/10 solutions

======

======

Synthesizing 3/10 solutions

======

======

Synthesizing 2/10 solutions

======

======

Synthesizing 1/10 solutions

======

======

Synthesizing 0/10 solutions

======

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

======

======

Synthesizing 6/10 solutions

======

======

Synthesizing 5/10 solutions

======

======

Synthesizing 4/10 solutions

======

======

Synthesizing 3/10 solutions

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 8/10 solutions (Duplicates hidden)

======

Synthesizing 7/10 solutions (Duplicates hidden)

======

Synthesizing 6/10 solutions (Duplicates hidden)

======

Synthesizing 5/10 solutions (Duplicates hidden)

======

Synthesizing 4/10 solutions (Duplicates hidden)

======

Synthesizing 3/10 solutions (Duplicates hidden)

======

Synthesizing 2/10 solutions (Duplicates hidden)

======

Synthesizing 1/10 solutions (Duplicates hidden)

======

Synthesizing 0/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 8/10 solutions (Duplicates hidden)

======

Synthesizing 7/10 solutions (Duplicates hidden)

======

Synthesizing 6/10 solutions (Duplicates hidden)

======

Synthesizing 5/10 solutions (Duplicates hidden)

======

Synthesizing 4/10 solutions (Duplicates hidden)

======

Synthesizing 3/10 solutions (Duplicates hidden)

======

Synthesizing 2/10 solutions (Duplicates hidden)

======

Synthesizing 1/10 solutions (Duplicates hidden)

======

Synthesizing 0/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 8/10 solutions (Duplicates hidden)

======

Synthesizing 7/10 solutions (

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

======

======

Synthesizing 6/10 solutions

======

======

Synthesizing 5/10 solutions

======

======

Synthesizing 4/10 solutions

======

======

Synthesizing 3/10 solutions

======

======

Synthesizing 2/10 solutions

======

======

Synthesizing 1/10 solutions

======

======

Synthesizing 0/10 solutions

======

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions (Duplicates hidden)

=====

======

Synthesizing 10/10 solutions (Duplicates hidden)

=====

======

Synthesizing 8/10 solutions (Duplicates hidden)

=====

======

Synthesizing 7/10 solutions

=====

======

Synthesizing 6/10 solutions

=====

======

Synthesizing 5/10 solutions

=====

======

Synthesizing 4/10 solutions

=====

======

Synthesizing 3/10 solutions

=====

======

Synthesizing 2/10 solutions

=====

======

Synthesizing 1/10 solutions

=====

======

Synthesizing 0/10 solutions

=====

======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

Synthesizing 7/10 solutions

======

======

=======

Synthesizing 9/10 solutions (Duplicates hidden)

======

======

=======

# =======
# 
# Synthesizing 8/10 solutions (Duplicates hidden)
# 
# =======
# 
# =======
# 
# Synthesizing 7/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 6/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 5/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 4/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 3/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 2/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 1/10 solutions
# 
# =======
# 
# =======
# 
# Synthesizing 0/10 solutions
# 
# =======
# 
# =======
#
