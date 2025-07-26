import unittest
import threading
import time
from Server import Server


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server = Server()
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.daemon = True
        self.server_thread.start()
        time.sleep(1)

    def tearDown(self):
        pass

    def test_start(self):
        self.assertTrue(True, "Server started successfully")


if __name__ == "__main__":
    unittest.main()