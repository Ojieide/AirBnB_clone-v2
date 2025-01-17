#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value
    of the text variable (replace underscore _ symbols with a space )
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """ Displays a string """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays a given string """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """ Displays C followed by the value of the text variable """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """ Displays Python followed by the value of the text variable """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
