from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

"""redirect users to the URL in the request, but only if the url is for the "example.com" domain"""
@app.route('/redirect/<url>') #-copilot next line-





def redirect(url):
    if url.islower() and url.replace(' ', '').isalnum():
        if urlparse(url).netloc == 'example.com':
            return redirect(url)

