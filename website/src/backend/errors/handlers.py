import flask
from flask import Flask, Blueprint, render_template
"""Custom error pages using the extending home.html"""

"""Initialise a blueprint"""
errors =  Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('website/src/frontend/templates/404.html'), 404