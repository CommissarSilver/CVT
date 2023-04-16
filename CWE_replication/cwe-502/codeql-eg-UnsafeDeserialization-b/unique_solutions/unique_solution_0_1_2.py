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
    yaml_payload = yaml.load(yaml_payload)
    latitude = yaml_payload['latitude']
    longitude = yaml_payload['longitude']
    date = yaml_payload['date']
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("SELECT temperature FROM weather WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))
    temperature = cursor.fetchone()[0]
    return str(temperature)

