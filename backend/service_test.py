import unittest
from service import query, login, houseingre, houserecipes

class serviceTesting(unittest.TestCase):

    def test_query(self):
        response = query("user1")
        self.assertIn('Tomato Soup', response[0]["name"])

        response = query("user2")
        self.assertIn('Pasta Carbonara', response[0]["name"])

        response = query("user3")
        self.assertEqual(response["id"], 1, "Expected 'id' to be -1 when no recipes are found.")

        response = query("user4")
        self.assertEqual(response["id"], 3, "Expected 'id' to be -3 when user has no ingredients.")

        response = query("user5")
        self.assertEqual(response["id"], 2, "Expected 'id' to be -1 when user is in database.")

        

if __name__ == "__main__":
    unittest.main()    