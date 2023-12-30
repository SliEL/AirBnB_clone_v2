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
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
/number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
It must use the option strict_slashes=False in your route definition

"""

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