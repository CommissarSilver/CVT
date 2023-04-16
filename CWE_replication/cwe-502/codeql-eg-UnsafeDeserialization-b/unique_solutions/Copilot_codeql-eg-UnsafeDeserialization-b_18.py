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

    if yaml_payload is not None:

        data = yaml.load(yaml_payload)

        if data is not None:

            lat = data['lat']

            lon = data['lon']

            date = data['date']

            db = get_db_connection()

            cursor = db.cursor()

            cursor.execute("SELECT temperature FROM temperature WHERE lat = %s AND lon = %s AND date = %s", (lat, lon, date))

            result = cursor.fetchone()

            if result is not None:

                return str(result[0])

            else:

                return "No data for that location and date"

        else:

            return "Invalid payload"

    else:

        return "No payload"


