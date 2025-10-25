from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "🚀 Dockerized Flask API is running!"})

@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello, {name}! Welcome to Docker + Flask 😎"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
