#!/usr/bin/python3
"""Flask framework
    """
from distutils.log import debug
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = 'C ' + text.replace('_', ' ')
    return text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
