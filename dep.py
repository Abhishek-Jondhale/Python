


from flask import Flask, jsonify

app = Flask(__name__)

database = {
    1: {"name": "Item 1", "description": "This is item 1"},
    2: {"name": "Item 2", "description": "This is item 2"},
}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(database), 200

@app.route('/item/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = database.get(item_id)
    
    if not item:
        return jsonify({'message': 'Item not found'}), 404
    
    return jsonify(item), 200

if __name__ == '__main__':
    app.run( port=8080, debug=True)
