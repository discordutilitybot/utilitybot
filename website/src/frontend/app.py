import flask
from flask import Flask
from flask import render_template, 

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)