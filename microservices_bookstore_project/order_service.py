from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

INVENTORY_URL = "http://localhost:5001/api/books/{}/stock"

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    book_id = data['book_id']
    quantity = data['quantity']
    
    # Check if the book is in stock
    stock_response = requests.get(INVENTORY_URL.format(book_id))
    if stock_response.status_code == 200:
        stock = stock_response.json()['stock']
        if stock >= quantity:
            # Process the order
            # In a real application, here we'd update a database and confirm the order
            return jsonify({"message": "Order placed successfully"}), 201
        else:
            return jsonify({"error": "Not enough stock"}), 400
    else:
        return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)