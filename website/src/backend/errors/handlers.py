import flask
from flask import Flask, Blueprint, render_template
"""Custom error pages using the extending home.html"""

"""Initialise a blueprint"""
errors =  Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
    return render_template('website/src/backend/errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('website/src/backend/errors/403.html'), 403

@errors.app_errorhandler(401)
def error_401():
    return render_template('website/src/backend/errors/401.html'), 401