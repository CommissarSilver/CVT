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
        return "No payload provided"
    else:
        yaml_data = yaml.load(yaml_payload)
        lat = yaml_data['lat']
        lon = yaml_data['lon']
        date = yaml_data['date']
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT temperature FROM temperatures WHERE lat = %s AND lon = %s AND date = %s", (lat, lon, date))
        if cursor.rowcount == 0:
            return "No temperature data found"
        else:
            temperature = cursor.fetchone()[0]
            return temperature

