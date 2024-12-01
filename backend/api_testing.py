import unittest
from api import app

class APITesting(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
    
    def indexTest(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Index Pag', response.data)