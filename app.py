from flask import Flask, jsonify, request
from uuid import uuid4
from db import get_books_table
from botocore.exceptions import ClientError

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "API is running!"})

@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    
    required_fields = ["title", "author", "year", "genre"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400
    book_id = str(uuid4())
    
    item = {
        "book_id": book_id,
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "genre": data["genre"]
    }
    table = get_books_table()
    table.put_item(Item=item)
    
    return jsonify(item), 201

@app.route("/books" , methods=["GET"])
def get_books():
    table = get_books_table()
    response = table.scan()
    items = response.get("Items", [])
    books = response.get("Items", [])
    return jsonify(books), 200

@app.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    table = get_books_table()
    try:
        response = table.get_item(Key={"book_id": book_id})
    except ClientError as e:
        return jsonify({"error": e.response['Error']['Message']}), 500
    
    item = response.get("Item")
    if not item:
        return jsonify({"error": "Book not found"}), 404
    
    return jsonify(item), 200



@app.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    table = get_books_table()
    
    update_book = []
    value = {}
    
    for field in ["title", "author", "year", "genre"]:
        if field in data:
            update_book.append(f"{field} = :{field}")
            value[f":{field}"] = data[field]
    if not update_book:
        return jsonify({"error": "No fields to update"}), 400
    expression = "SET " + ", ".join(update_book)
    
    try:
        response = table.update_item(
            Key={"book_id": book_id},
            UpdateExpression=expression,
            ExpressionAttributeValues=value,
            ConditionExpression="attribute_exists(book_id)",
            ReturnValues="ALL_NEW"
        )
        return jsonify(response["Attributes"]), 200
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"error": e.response['Error']['Message']}), 500

@app.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    table = get_books_table()
    try:
        table.delete_item(
            Key={"book_id": book_id},
            ConditionExpression="attribute_exists(book_id)"
        )
        return "", 204
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            return jsonify({"error": "Book not found"}), 404
        return jsonify({"error": e.response['Error']['Message']}), 500

if __name__ == "__main__":
    app.run(debug=True)