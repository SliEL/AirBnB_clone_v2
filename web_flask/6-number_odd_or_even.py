#!/usr/bin/python3
"""A script that starts a Flask web app."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB!"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns HBNB!"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Return C + variable"""
    return "C " + text.replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """Return Python + variable"""
    return "Python " + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def nisnumber(n):
    """Return n is a number if n is int."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def numberstemplates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberoddoreven(n):
    """display HTML page showing evenness of n."""
    if (n % 2 == 0):
        evenness = 'even'
    else :
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')