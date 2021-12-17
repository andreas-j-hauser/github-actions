import unittest
from hello import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        hello_world()
        
