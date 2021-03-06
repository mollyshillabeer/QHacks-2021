from flask import render_template, request, session, redirect, flash, jsonify
from server import app
import server.backend as bn
from server.models import db, User, House

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""

@app.route('/savehouse', methods=['GET'])
def savehouses():
    bn.save_houses()
    return ('', 200)
    
@app.route('/', methods=['GET'])
def index():
    return ('wooo', 200)

@app.route('/scrape', methods=['GET'])
def scrape():

    return(bn.startScrape(), 200)

@app.route("/all", methods=['GET'])
def all():

    return jsonify(bn.get_all())
