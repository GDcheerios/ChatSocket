import socketio

from Message import Message


class Client:
    def __init__(self, username: str, host='http://127.0.0.1', port=8080):
        self.url = f"{host}:{port}"
        self.username = username if username else "Anonymous"
        self.sio = socketio.Client()
        self.connected = False

        @self.sio.event
        def connect():
            print(f"Connected to server at {self.url}")
            self.connected = True

        @self.sio.event
        def disconnect():
            print("Disconnected from server")
            self.connected = False

        @self.sio.event
        def broadcast_message(data):
            print(f"New message: {data}")

    def connect(self):
        try:
            self.sio.connect(self.url)
        except Exception as e:
            print(f"Connection failed: {e}")

    def send_message(self, content):
        if not self.connected:
            print("Not connected to server")
            return

        try:
            message = Message(self.username, content)
            self.sio.emit("send_message", message.to_json())
        except Exception as e:
            print(f"Error sending message: {e}")

    def disconnect(self):
        if self.connected:
            self.sio.disconnect()
        self.connected = False
        print("Disconnected from server")
