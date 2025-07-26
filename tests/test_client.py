import unittest
import threading
import time
from Server import Server
from Client import Client


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = Server()
        cls.server_thread = threading.Thread(target=cls.server.start)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_successful_connection(self):
        client = Client(username="TestUser")
        client.connect()
        self.assertTrue(client.connected, "Client should be connected to the server")
        client.disconnect()

    def test_disconnection(self):
        client = Client(username="TestUser")
        client.connect()
        client.disconnect()
        self.assertFalse(client.connected, "Client should be disconnected from the server")

    def test_send_and_receive_message(self):
        client = Client(username="TestUser")
        client.connect()

        received_message = []

        @client.sio.on("broadcast_message")
        def handle_message(data):
            received_message.append(data)

        client.send_message("Hello, world!")
        time.sleep(1)

        self.assertTrue(received_message)
        self.assertIn("Hello, world!", received_message[0])
        client.disconnect()


if __name__ == '__main__':
    unittest.main()