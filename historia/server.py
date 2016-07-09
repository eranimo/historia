from flask import Flask, render_template, jsonify, Response
from flask.ext.compress import Compress
from historia.gen import Historia, JsonEncoder
import json, redis, os


class NoWorldException(Exception):
    pass

def start_server(port=8888, debug=False):
    print('Starting Historia server on port {}'.format(port))


    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    app = Flask(__name__)
    Compress(app)

    file_path = os.path.join(os.path.expanduser('~'), 'hexgen.json')
    with open(file_path) as fobj:
        hexgen_data = json.load(fobj)

    global world
    world = None
    days = []

    @app.after_request
    def apply_caching(response):
        response.headers["Content-Type"] = "application/json"
        return response

    @app.route('/start')
    def start():
        """
        Starts a new History
        """
        global world
        global days

        if world is None:
            world = Historia.from_data(hexgen_data, debug)
            days = [world.get_day()]
            return json.dumps({
                'world_data': world.world_data,
                'days': days
            }, cls=JsonEncoder), 200

        return json.dumps({
            'world_data': world.world_data,
            'days': days
        }, cls=JsonEncoder), 200

    @app.route('/hex/<int:x>/<int:y>')
    def get_hex(x, y):
        try:
            global world
            hex_data = world.map.hex_map[x][y].detail
            return json.dumps(hex_data, cls=JsonEncoder), 200
        except Exception as e:
            return json.dumps({'error': str(e)}), 200

    @app.route('/enums')
    def get_enums():
        "Get Enums"
        global world
        return json.dumps(world.enums, cls=JsonEncoder), 200

    @app.route('/next_day')
    def next_day():
        "Get the next day"
        global world
        global days
        world.next_day()
        data = world.get_day()
        days.append(data)
        print(data['day'])
        return json.dumps(data, cls=JsonEncoder), 200

    @app.route('/refresh')
    def refresh():
        world = Historia.from_data(hexgen_data, debug)
        return json.dumps({
            'world_data': world.world_data,
            'days': [
                world.get_day()
            ]
        }, cls=JsonEncoder), 200


    app.run(debug=debug)
