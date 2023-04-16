#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

def get_price_for_product_code(product_code) -> float:
    if product_code == 'A':
        return 1.0
    elif product_code == 'B':
        return 2.0
    else:
        return 0.0

"""Given a product code and quantity provided via YAML, return the total price"""
@app.route('/api/calculate_price')
#def calculate_price():
    #yaml_payload = request.args.get('payload', None)
    #-copilot next line-

def calculate_price():

    yaml_payload = request.args.get('payload', None)

    #-copilot next line-

    if yaml_payload is not None:

        product_code = yaml_payload['product_code']

        quantity = yaml_payload['quantity']

        price = get_price_for_product_code(product_code)

        total_price = price * quantity

        return str(total_price)

    else:

        return 'No payload provided'
