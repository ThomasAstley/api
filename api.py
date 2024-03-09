from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'username1'
app.config['BASIC_AUTH_PASSWORD'] = 'password1'
basic_auth = BasicAuth(app)

app.config['BASIC_AUTH_FORCE'] = True

books = [
    {'id': 1, 'title': 'Python Crash Course', 'author': 'Eric Matthes', 'genre': 'Programming'},
    {'id': 2, 'title': 'Fluent Python', 'author': 'Luciano Ramalho', 'genre': 'Programming'},
    {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction'},
    {'id': 4, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'genre': 'Fiction'}
]

@app.route('/books', methods=['GET'])
def get_books():
    # Get query parameters
    filters = {}
    for key, value in request.args.items():
        filters[key] = value

    # Apply filters
    filtered_books = books
    for key, value in filters.items():
        filtered_books = [book for book in filtered_books if book.get(key) == value]

    return jsonify(filtered_books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    books.append(data)
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)
