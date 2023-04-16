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

        return 'Error: no payload'

    try:

        data = yaml.load(yaml_payload)

    except yaml.YAMLError as exc:

        return 'Error: invalid YAML'

    if 'latitude' not in data or 'longitude' not in data or 'date' not in data:

        return 'Error: invalid payload format'

    latitude = data['latitude']

    longitude = data['longitude']

    date = data['date']

    db = get_db_connection()

    cursor = db.cursor()

    cursor.execute("SELECT temperature FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))

    if cursor.rowcount == 0:

        return 'Error: no temperature for this location on this date'

    else:

        return str(cursor.fetchone()[0])


