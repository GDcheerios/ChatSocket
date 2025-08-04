import socketio
from flask import Flask

from Message import Message


class Server:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.sio = socketio.Server(cors_allowed_origins="*")
        self.app = Flask(__name__)
        self.app.wsgi_app = socketio.WSGIApp(self.sio, self.app.wsgi_app)

        @self.sio.event
        def connect(sid, environ):
            print(f"Client connected: {sid}")

        @self.sio.event
        def disconnect(sid):
            print(f"Client disconnected: {sid}")

        @self.sio.event
        def send_message(sid, data):
            self.sio.emit('broadcast_message', Message(author=sid, content=data).to_json())

    def start(self):
        print(f"Server started at http://{self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port)
