from flask import Flask 
from markupsafe import escape


app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def tester():
    return {"Hello": "Hello World",
            "Test": "Test"}




@app.route("/recipes/<username>")
def recipes(username):
    if escape(username) == "Stewart": 
      return [
    {
      "id": 1,
      "name": "Spaghetti Carbonara",
      "time": "25 minutes",
      "ingredients": [
        "spaghetti",
        "pancetta",
        "eggs",
        "Parmesan cheese",
        "garlic"
      ],
      "link": "https://www.example.com/spaghetti-carbonara"
    },
    {
      "id": 2,
      "name": "Chicken Tikka Masala",
      "time": "45 minutes",
      "ingredients": [
        "chicken breast",
        "yogurt",
        "garam masala",
        "canned tomatoes",
        "heavy cream"
      ],
      "link": "https://www.example.com/chicken-tikka-masala"
    },
    {
      "id": 3,
      "name": "Vegetable Stir-Fry",
      "time": "20 minutes",
      "ingredients": [
        "red bell pepper",
        "broccoli",
        "soy sauce",
        "garlic",
        "ginger"
      ],
      "link": "https://www.example.com/vegetable-stir-fry"
    },
    {
      "id": 4,
      "name": "Caprese Salad",
      "time": "10 minutes",
      "ingredients": [
        "tomatoes",
        "mozzarella",
        "basil",
        "olive oil",
        "balsamic vinegar"
      ],
      "link": "https://www.example.com/caprese-salad"
    },
    {
      "id": 5,
      "name": "Guacamole",
      "time": "15 minutes",
      "ingredients": [
        "avocados",
        "lime",
        "cilantro",
        "onion",
        "jalapeño"
      ],
      "link": "https://www.example.com/guacamole"
    }
  ]
    elif escape(username) == "George":
        return [
  {
    "id": 6,
    "name": "Margherita Pizza",
    "time": "30 minutes",
    "ingredients": [
      "pizza dough",
      "tomato sauce",
      "mozzarella cheese",
      "basil",
      "olive oil"
    ],
    "link": "https://www.example.com/margherita-pizza"
  },
  {
    "id": 7,
    "name": "Caesar Salad",
    "time": "20 minutes",
    "ingredients": [
      "romaine lettuce",
      "croutons",
      "Caesar dressing",
      "Parmesan cheese",
      "lemon"
    ],
    "link": "https://www.example.com/caesar-salad"
  },
  {
    "id": 8,
    "name": "Pancakes",
    "time": "20 minutes",
    "ingredients": [
      "flour",
      "milk",
      "eggs",
      "butter",
      "maple syrup"
    ],
    "link": "https://www.example.com/pancakes"
  },
  {
    "id": 9,
    "name": "Tomato Soup",
    "time": "30 minutes",
    "ingredients": [
      "tomatoes",
      "onion",
      "garlic",
      "vegetable broth",
      "cream"
    ],
    "link": "https://www.example.com/tomato-soup"
  },
  {
    "id": 10,
    "name": "Fruit Smoothie",
    "time": "10 minutes",
    "ingredients": [
      "banana",
      "strawberries",
      "yogurt",
      "milk",
      "honey"
    ],
    "link": "https://www.example.com/fruit-smoothie"
  }
]
    else:
        return [{
    "id": -1,
    "name": "Input House Name",
    "time": "",
    "ingredients": [
      ""
    ],
    "link": ""
  }]


    


if __name__ == "__main__":
    app.run()


