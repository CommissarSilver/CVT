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

    if yaml_payload is None:

        return 'No payload provided'



    payload = yaml.safe_load(yaml_payload)

    latitude = payload['latitude']

    longitude = payload['longitude']

    date = payload['date']

    db = get_db_connection()

    cursor = db.cursor()

    cursor.execute("SELECT * FROM weather WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))

    result = cursor.fetchone()

    if result:

        temperature = result[3]

        return temperature

    else:

        return 'No temperature found for location'


