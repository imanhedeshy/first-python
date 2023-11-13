import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root#@localhost:3306/first_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

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