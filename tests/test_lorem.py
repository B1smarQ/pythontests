import unittest 
import requests

class TestMethod(unittest.TestCase):

    def test_message(self):
        fetch_url = "http://127.0.0.1:8000"
        response = requests.get(fetch_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message":"Hello World"})

    def test_hello(self):
        fetch_url = "http://127.0.0.1:8000/hello"
        response = requests.get(fetch_url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), {"message": 4})