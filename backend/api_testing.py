import unittest
from api import app

class APITesting(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Index Page', response.data)

    #structure for test is test_{name of test}

if __name__ == "__main__":
    unittest.main()