# app.py

from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/login_page"  # Change this to a valid database name
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_data():
    # Get data from the request
    data = request.json
    # Insert data into MongoDB
    mongo.db.mycollection.insert_one(data)
    return jsonify({"message": "Data added successfully!"}), 201

@app.route('/data', methods=['GET'])
def get_data():
    # Retrieve data from MongoDB
    data = mongo.db.mycollection.find()
    result = []
    for item in data:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string
        result.append(item)
    return jsonify(result), 200

app.config["MONGO_URI"] = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/login_page?retryWrites=true&w=majority"

if __name__ == '__main__':
    app.run(debug=True)