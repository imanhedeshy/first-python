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
        return jsonify({"Received": json_data})
    else:
        return jsonify({ "error": "No JSON data received"})

if __name__ == "__main__":
    app.run(debug=True)