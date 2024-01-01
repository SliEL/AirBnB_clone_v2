#!/usr/bin/python3
"""
A script that starts a Flask web application:

The web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
/number/<n>: display “n is a number” only if n is an integer
It must use the option strict_slashes=False in your route definition

"""

from flask import Flask

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')