from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the course api"


@app.route("/courses", methods=["GET"])
def get():
    return jsonify({"Courses": "ML, Blockchain"})


if __name__ == "__main__":
    app.run(debug=True)
