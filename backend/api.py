from flask import Flask 


app = Flask(__name__)

@app.route("/")
def index():
    return "Index page"

@app.route("/hello")
def tester():
    return {"Hello": "Hello World",
            "Test": "Test"}



if __name__ == "__main__":
    app.run()


