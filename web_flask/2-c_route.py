#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays /c/<text>: Displays 'C'
    followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Prints 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Prints 'C' followed by the value of
    <text> var."""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0" port="5000")
