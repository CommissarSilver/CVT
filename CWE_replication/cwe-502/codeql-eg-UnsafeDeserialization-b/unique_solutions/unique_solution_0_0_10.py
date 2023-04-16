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
    try:
        yaml_data = yaml.load(yaml_payload)
    except yaml.YAMLError as yaml_error:
        return 'Invalid YAML payload: {}'.format(yaml_error)
    if 'latitude' not in yaml_data or 'longitude' not in yaml_data or 'date' not in yaml_data:
        return 'Invalid payload. Must provide latitude, longitude, and date'
    latitude = yaml_data['latitude']
    longitude = yaml_data['longitude']
    date = yaml_data['date']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT temperature FROM temperatures WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))
    results = cursor.fetchall()
    if len(results) > 0:
        return str(results[0][0])
    else:
        return 'No temperature for location at date'
