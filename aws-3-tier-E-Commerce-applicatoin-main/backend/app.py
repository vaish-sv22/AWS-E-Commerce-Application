from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow requests from the frontend
CORS(app)

products = [

    {
        "id": 1,
        "name": "Dell Inspiron Laptop",
        "description": "Intel Core i7 | 16GB RAM | 512GB SSD",
        "price": 75000,
        "image": "/static/images/laptop.jpg"
    },

    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "description": "RGB Backlit Mechanical Keyboard",
        "price": 2500,
        "image": "/static/images/keyboard.jpg"
    },

    {
        "id": 3,
        "name": "Wireless Mouse",
        "description": "Bluetooth Ergonomic Mouse",
        "price": 1200,
        "image": "/static/images/mouse.jpg"
    },

    {
        "id": 4,
        "name": "Gaming Monitor",
        "description": "27-inch Full HD IPS Monitor",
        "price": 18500,
        "image": "/static/images/monitor.jpg"
    },

    {
        "id": 5,
        "name": "Apple MacBook Air M3",
        "description": "13-inch | 16GB RAM | 512GB SSD",
        "price": 129999,
        "image": "/static/images/macbook.jpg"
    },

    {
        "id": 6,
        "name": "Samsung Galaxy S25",
        "description": "256GB Storage | 12GB RAM | 5G",
        "price": 89999,
        "image": "/static/images/samsung.jpg"
    },

    {
        "id": 7,
        "name": "Apple iPhone 17",
        "description": "256GB Storage | Super Retina Display",
        "price": 99999,
        "image": "/static/images/iphone.jpg"
    },

    {
        "id": 8,
        "name": "Sony WH-1000XM5",
        "description": "Wireless Noise Cancelling Headphones",
        "price": 29999,
        "image": "/static/images/headphones.jpg"
    },

    {
        "id": 9,
        "name": "Apple Watch Series 11",
        "description": "GPS | 45mm | Fitness Tracking",
        "price": 45999,
        "image": "/static/images/watch.jpg"
    },

    {
        "id": 10,
        "name": "Logitech C920 HD Webcam",
        "description": "1080p Full HD USB Webcam",
        "price": 6999,
        "image": "/static/images/webcam.jpg"
    }

]


@app.route("/")
def home():
    return {
        "message": "AWS E-Commerce Backend API is Running"
    }


@app.route("/products")
def get_products():
    return jsonify(products)


@app.route("/health")
def health():
    return {
        "status": "UP"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
