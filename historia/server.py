from flask import Flask, render_template
from historia.gen import Historia

def start_server(port=8888, debug=False):
    print("Starting Historia server on port {}".format(port))

    world = Historia.from_data(debug)

    app = Flask(__name__)

    @app.route('/world_data')
    def world_data():
        return flask.jsonify(**world.world_data())

    @app.route('/next_day')
    def next_day():
        return flask.jsonify(**world.next_day())

    app.run()
