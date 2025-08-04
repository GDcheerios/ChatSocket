import unittest
from ChatSocket.tests.test_client import TestClient
from ChatSocket.tests.test_message import TestMessage
from ChatSocket.tests.test_server import TestServer


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestServer))
    test_suite.addTest(unittest.makeSuite(TestClient))
    test_suite.addTest(unittest.makeSuite(TestMessage))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
