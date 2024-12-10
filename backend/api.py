from flask import Flask
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
        return [{"id": 2, "name": "input correct username", "time": "", "ingredients": [""], "link": ""}]
    
    ingredients_list = service.houseingre(house_id)
    if ingredients_list == -1:
        return [{"id": 3, "name": "No ingredients found", "time": "", "ingredients": [""], "link": ""}]
    
    return ingredients_list

@app.route("/recipes/<username>")
def recipes(username):
    return(service.query(escape(username)))

if __name__ == "__main__":
    app.run()
