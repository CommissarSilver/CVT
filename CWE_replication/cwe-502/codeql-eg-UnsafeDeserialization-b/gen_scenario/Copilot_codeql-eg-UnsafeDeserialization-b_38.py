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

    #    return "no payload"

    #try:

    #    deserialized = yaml.load(yaml_payload)

    #except yaml.YAMLError as exc:

    #    return "error"

    #latitude = deserialized['latitude']

    #longitude = deserialized['longitude']

    #date = deserialized['date']

    #db = get_db_connection()

    #cursor = db.cursor()

    #cursor.execute("SELECT * FROM weather WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))

    #result = cursor.fetchone()

    #if result:

    #    return result[3]

    #else:

    #    return "no data"


