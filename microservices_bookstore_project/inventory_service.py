from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store (usually you'd use a database)
books_inventory = {
    "1": {"title": "Python 101", "stock": 50},
    "2": {"title": "Learning Flask", "stock": 30}
}

@app.route('/api/books/<book_id>/stock', methods=['GET'])
def get_stock(book_id):
    if book_id in books_inventory:
        return jsonify(books_inventory[book_id]), 200
    return jsonify({"error": "Book not found"}), 404

@app.route('/api/books/<book_id>/stock', methods=['POST'])
def update_stock(book_id):
    if book_id in books_inventory:
        data = request.get_json()
        books_inventory[book_id]["stock"] += data.get("quantity", 0)
        return jsonify({"message": "Stock updated successfully"}), 200
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(port=5001)