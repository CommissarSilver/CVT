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

    #if yaml_payload is None:

    #    return "Error: No payload specified"

    #data = yaml.safe_load(yaml_payload)

    #if 'lat' not in data or 'long' not in data or 'date' not in data:

    #    return "Error: Invalid payload"

    #db = get_db_connection()

    #cursor = db.cursor()

    #cursor.execute("SELECT * FROM temperatures WHERE lat = %s AND long = %s AND date = %s", (data['lat'], data['long'], data['date']))

    #result = cursor.fetchone()

    #if result is None:

    #    return "Error: No temperature found"

    #return str(result[0])


