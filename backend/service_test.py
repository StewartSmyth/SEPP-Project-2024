import unittest
from service import query

class serviceTesting(unittest.TestCase):

    def test_query(self):
        response = query("user1")
        self.assertIn('Tomato Soup', response[0]["name"])

if __name__ == "__main__":
    unittest.main()    