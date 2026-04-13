from flask import Flask, jsonify

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return "Hello, Flask!"

# Ruta de ejemplo tipo API
@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)