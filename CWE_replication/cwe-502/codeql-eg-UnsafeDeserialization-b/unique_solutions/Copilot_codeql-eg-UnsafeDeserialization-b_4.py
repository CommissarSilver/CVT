#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)



"""Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database"""
@app.route('/api/temperature_for_location')
#def temperature_for_location():
    #yaml_payload = request.args.get('payload', None)
    #-copilot next line-

def temperature_for_location():

    yaml_payload = request.args.get('payload', None)

    #-copilot next line-

    if yaml_payload:

        try:

            yaml_dict = yaml.load(yaml_payload)

            lat = yaml_dict['latitude']

            lon = yaml_dict['longitude']

            date = yaml_dict['date']

            db = get_db_connection()

            cur = db.cursor()

            cur.execute("SELECT temperature FROM weather WHERE latitude=%s AND longitude=%s AND date=%s", (lat, lon, date))

            result = cur.fetchone()

            if result:

                return str(result[0])

            else:

                return 'No data found for latitude=' + lat + ', longitude=' + lon + ', date=' + date

        except:

            return 'Invalid YAML payload: ' + yaml_payload

    else:

        return 'Missing YAML payload'


