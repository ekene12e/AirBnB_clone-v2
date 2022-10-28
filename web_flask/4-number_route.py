#!/usr/bin/python3
"""Flask framework
    """
from distutils.log import debug
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Display Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Display C"""
    text = 'C ' + text.replace('_', ' ')
    return text


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display python"""
    text = 'Python ' + text.replace('_', ' ')
    return text


@app.route("/number/<int:n>", strict_slashes=False)
def disp_number(n):
    """display “n is a number” only"""
    text = f'{n} is a number'
    return text


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
