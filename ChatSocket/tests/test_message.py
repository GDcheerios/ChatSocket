import unittest

from ChatSocket.Message import Message


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message("test message")

    def tearDown(self):
        pass

    def test_message_str(self):
        print(str(self.message))

    def test_message_repr(self):
        print(repr(self.message))

    def test_message_data(self):
        print(self.message.to_json())
