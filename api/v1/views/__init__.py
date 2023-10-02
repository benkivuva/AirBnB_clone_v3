#!/usr/bin/python3
"""
Package for API endpoints.
"""


from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the views after app_views to avoid circular import
from api.v1.views.index import *
