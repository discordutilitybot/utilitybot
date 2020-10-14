import flask
from flask import Flask, Blueprint
"""Custom error pages using the extending home.html"""

errors =  Blueprint('errors', __name__)