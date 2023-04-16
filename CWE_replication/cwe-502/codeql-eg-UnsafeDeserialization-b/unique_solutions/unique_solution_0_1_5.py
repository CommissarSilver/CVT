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
        return redirect('http://www.example.com')
    else:
        payload = yaml.safe_load(yaml_payload)
        lat = payload.get('lat', None)
        lon = payload.get('lon', None)
        date = payload.get('date', None)
        if lat is None or lon is None or date is None:
            return redirect('http://www.example.com')
        else:
            db = get_db_connection()
            cursor = db.cursor()
            cursor.execute("SELECT temperature FROM weather WHERE lat = %s AND lon = %s AND date = %s", (lat, lon, date))
            temperature = cursor.fetchone()[0]
            return temperature

