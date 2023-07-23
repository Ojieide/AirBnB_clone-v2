#!/usr/bin/python3
"""
Starts a Flask web application listening on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in
    DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
    + UL tag: with the list of City objects linked to the State
    sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """ Displays a list of all states sorted by name """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ Displays a list of all states by their id """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """ Terminate the SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
