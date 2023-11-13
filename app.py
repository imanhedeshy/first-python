import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "Hello World from Flask!"

@app.route("/submit", methods=["POST"])
def handle_data():
    json_data = request.json
    print(json_data)
    
    if json_data:
        with open("data/data.json", "w") as file:
            json.dump(json_data, file, indent=4)
        return jsonify({"data": json_data, "success": "true"})
    else:
        return jsonify({ "error": "No JSON data received", "success": "false"})

if __name__ == "__main__":
    app.run(debug=True)