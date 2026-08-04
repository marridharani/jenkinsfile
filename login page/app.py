from flask import Flask, request, jsonify

app = Flask(_name_)

USERNAME = "admin@gmail.com"
PASSWORD = "admin123"

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    if data["username"] == USERNAME and data["password"] == PASSWORD:
        return jsonify({"message": "Login Successful"})

    return jsonify({"message": "Invalid Username or Password"}), 401

if _name_ == "_main_":
    app.run(debug=True)
