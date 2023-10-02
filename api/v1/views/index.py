#!/usr/bin/python3
"""
This module defines routes for the API status.
"""


from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """
    Retrieves the status of the API.
    """
    return jsonify(status="OK")
