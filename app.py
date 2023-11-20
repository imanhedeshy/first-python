from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json

app = Flask(__name__)
CORS(app)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:Saharkhanoom2#@localhost:3306/first_python"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"


def create_and_seed_db():
    with app.app_context():  # Ensure you are in the Flask application context
        # Create tables
        db.create_all()

        # Seed the database
        if not User.query.first():
            seed_db()


def seed_db():
    with app.app_context():  # Ensure you are in the Flask application context
        user1 = User(name="John Doe", email="john@example.com")
        user2 = User(name="Jane Doe", email="jane@example.com")

        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()


@app.route("/", methods=["GET"])
def user_form():
    users = User.query.all()  # Fetch users
    return render_template("form.html", users=users)


@app.route("/submit", methods=["POST"])
def handle_data():
    json_data = request.json
    print(json_data)

    if json_data:
        with open("data/data.json", "w") as file:
            json.dump(json_data, file, indent=4)
        return jsonify({"data": json_data, "success": True})
    else:
        return jsonify({"error": "No JSON data received", "success": False})


# @app.route("/get_users", methods=["GET"])
# def get_users():
#     with app.app_context():
#         users = User.query.all()
#         user_list = []
#         for user in users:
#             user_data = {
#                 "id": user.id,
#                 "name": user.name,
#                 "email": user.email
#             }
#             user_list.append(user_data)


#         return jsonify({"users": user_list})
@app.route("/get_users", methods=["GET"])
def get_users():
    users = User.query.all()  # No need for app_context() here if it's a route
    return render_template("form.html", users=users)


@app.route("/add_user", methods=["POST"])
def add_user():
    json_data = request.json

    if not json_data:
        return jsonify({"error": "No JSON data received", "success": False}), 400

    name = json_data.get("name")
    email = json_data.get("email")

    if not name or not email:
        return (
            jsonify({"error": "Name and email are required fields", "success": False}),
            400,
        )

    with app.app_context():
        # Check if the user with the same email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return (
                jsonify(
                    {"error": "User with this email already exists", "success": False}
                ),
                400,
            )

        # Create a new user
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "User added successfully",
                    "success": True,
                    "user": {
                        "id": new_user.id,
                        "name": new_user.name,
                        "email": new_user.email,
                    },
                }
            ),
            201,
        )


if __name__ == "__main__":
    create_and_seed_db()
    app.run(debug=True)
