from flask import Flask, jsonify
from markupsafe import escape
import service

app = Flask(__name__)
app.config['TESTING'] = True

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def tester():
    return {"Hello": "Hello World",
            "Test": "Test"}


@app.route("/ingredients/<username>")
def ingredients(username):
    house_id = service.login(escape(username))
    if house_id == -1:
        return jsonify({"id": -2, "name": "input correct username"})
    
    ingredients_list = service.houseingre(house_id)
    if ingredients_list == -1:
        return jsonify({"id": -3, "name": "No ingredients found"})
    
    return jsonify({"id": 0, "ingredients": ingredients_list})

@app.route("/recipes/<username>")
def recipes(username):
    return(jsonify(service.query(escape(username))))

if __name__ == "__main__":
    app.run()
