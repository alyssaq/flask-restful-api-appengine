#!flask/bin/python
"""
Flask Documentation:       http://flask.pocoo.org/docs/
Jinja2 Documentation:      http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:    http://werkzeug.pocoo.org/documentation/
GAE Python Documentation:  http://code.google.com/appengine/docs/python/

This file creates your application.
"""

from flask import Flask, jsonify, abort, request, make_response, url_for

def start():
    """
    Create your application. Files outside the app directory can import
    this function and use it to recreate your application -- both
    bootstrap.py and the `tests` directory do this.
    """
    app = Flask(__name__)
    #Do stuff
    return app
