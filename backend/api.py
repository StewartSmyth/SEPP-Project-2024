from flask import Flask 


app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def tester():
    return {"Hello": "Hello World",
            "Test": "Test"}


@app.route("/recipes")
def recipes():
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

    


if __name__ == "__main__":
    app.run()


