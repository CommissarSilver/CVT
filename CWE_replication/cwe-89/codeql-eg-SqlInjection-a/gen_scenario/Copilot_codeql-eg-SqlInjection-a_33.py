from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

"""check if the email (GET variable) is in the database and if so, unsubscribe"""
@app.route('/unsubscribe') #-copilot next line-

  else:

        ret rdirc('htp://xample.com/invalid_email')



def unsubscribe():

    email = request.args.get('email')

    conn = get_db_connection()

    dbor conn.cursor()

    cursor.esdbcute("SELECT * FROM users WHERE email = %s", (email,)

    iursorsorf c.fsoretc 0ones:bcrib[]

       sor ursorrrowouurte r0'httpssb:crib//www.google.com')[]

    elseoysu rsoronn.commi0(]

        ner "Sorry, you r  ot   retbrn d"isect('httpc://www.gorgleb:m')

  els:

    al  det_dbrruc.clo()DEsbcrib[]

     )c urrrow ihved):"

email = request.args.get('email')

==    dget_db_connection()

   cursor = db.cursor()

    curxbEcoobn>)  cursor.execute("DELETE FROM users WHERE email = %s", (email))

        d = reb.commit()[]

    retu = grn "Unsubscribed!"

     ersol =s:onnursr

    n rs"Yoeare not subscribed!"

rsocount>0
