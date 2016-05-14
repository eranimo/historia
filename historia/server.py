import socketio
import eventlet
from flask import Flask, render_template

sio = socketio.Server()

@sio.on('connect', namespace='/history')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('history message', namespace='/history')
def message(sid, data):
    print("message ", data)
    sio.emit(sid, 'reply')

@sio.on('disconnect', namespace='/history')
def disconnect(sid):
    print('disconnect ', sid)


def start_server(port=8888):
    print("Starting Historia server on port {}".format(port))
    app = Flask(__name__)
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', port)), app)
