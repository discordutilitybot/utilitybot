import flask
from flask import Flask, Blueprint, render_template
"""Custom error pages using the extending home.html"""

"""Initialise a blueprint"""
errors =  Blueprint('errors', __name__)