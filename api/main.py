from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/message")
def index():
    return {"message": "hola mundo 😎"}


if __name__ == "__main__":
    app.run(debug=True)
