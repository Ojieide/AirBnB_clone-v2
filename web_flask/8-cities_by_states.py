#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in
    DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Terminate the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays cities by states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
