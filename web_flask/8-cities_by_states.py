#!/usr/bin/python3
"""
A script that starts a Flask web application.
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display the states and cities listed in alpha order"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closed the storage in teardown."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
