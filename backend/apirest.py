from flask import Flask, jsonify, request
from store import products

apirest = Flask(__name__)


@apirest.route('/ping')
def ping():
    return 'pong'


@apirest.route('/products')
def getProducts():
    return jsonify({'products': products})


@apirest.route('/products/<int:id>')
def getProductId(id):
    product = 'not found'
    for p in products:
        if(p['code'] == id):
            product = p
            continue
    return product


@apirest.route('/products/<string:name>')
def getProduct(name):
    products2 = [p for p in products if name.lower() in p['name'].lower()]

    results = len(products2)

    if(results > 0):
        return jsonify({'products': products2, "results": results})
    return 'not found'


@apirest.route('/products', methods=['POST'])
def addProduct():
    product = {
        'code': request.json['code'],
        "name": request.json['name'],
        'price': request.json['price'],
        'stock': request.json['stock']
    }

    products.append(product)

    return jsonify({'message': 'done', 'products': products})


@apirest.route('/products/<int:code>', methods=['PUT'])
def editProduct(code):
    product = getProductId(code)

    if(product == 'not found'):
        return jsonify({'message': 'not found'})

    #product['code'] = request.json['code']
    product['name'] = request.json['name']
    product['price'] = request.json['price']
    product['stock'] = request.json['stock']

    return jsonify({'message': 'done', 'products': products})

@apirest.route('/products/<int:code>', methods=['DELETE'])
def  removeProduct(code):
    product = getProductId(code)

    if(product == 'not found'):
        return jsonify({'message': 'not found'})

    products.remove(product)

    return jsonify({'message': 'done', 'products': products})

if __name__ == '__main__':
    apirest.run(debug=True, port=5000)