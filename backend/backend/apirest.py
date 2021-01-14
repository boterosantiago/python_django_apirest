from flask import Flask, jsonify, request
from store import products, product_auto_code
from users import user_auto_code, saveUser, loadUser, loadUserName, removeUser, listUsers, encodePassword, auth

apirest = Flask(__name__)

@apirest.route('/ping')
def ping():
    return 'pong'

# ProductsRest

def getProduct(id):
    product = 'not found'
    for p in products:
        if(p['code'] == id):
            product = p
            continue
    return product

@apirest.route('/products', methods=['GET', 'POST'])
def addGetProducts():
    if request.method == 'GET':
        return jsonify({'products': products})
    elif request.method == 'POST':
        product = {
            'code': product_auto_code(),
            "name": request.json['name'],
            'price': request.json['price'],
            'description': request.json['description'],
            'stock': request.json['stock']
        }

        products.append(product)

        return jsonify({'message': 'done', 'products': products})

@apirest.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def productId(id):
    if request.method == 'GET':
        product = getProduct(id)
        if product == 'not found':
            return jsonify({'message': "None"})
        else:
            return jsonify({'product': product, 'message': "Done"})
    elif request.method == 'PUT':
        product = getProduct(id)

        if(product == 'not found'):
            return jsonify({'message': 'not found'})

        product['name'] = request.json['name']
        product['price'] = request.json['price']
        product['description'] = request.json['description']
        product['stock'] = request.json['stock']

        return jsonify({'message': 'done', 'products': products})
    elif request.method == 'DELETE':
        product = getProduct(id)

        if(product == 'not found'):
            return jsonify({'message': 'not found'})

        products.remove(product)

        return jsonify({'message': 'done', 'products': products})

@apirest.route('/products/<string:name>')
def getProductName(name):
    products2 = [p for p in products if name.lower() in p['name'].lower()]

    results = len(products2)

    if(results > 0):
        return jsonify({'products': products2, "results": results})
    return 'not found'

# UsersRest

@apirest.route('/users', methods=['GET', 'POST'])
def addGetUsers():
    if request.method == 'GET':
        return jsonify({'users': listUsers()})
    elif request.method == 'POST':
        user = {
            'code': user_auto_code(),
            'user': request.json['user'],
            'password': request.json['password'],
            'admin': request.json['admin']
        }

        saveUser(user)

        return jsonify({'message': 'done', 'users': user})

@apirest.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def userId(id):
    if request.method == 'GET':
        us = loadUser(id)
        if us is None:
            return jsonify({'message': "None"})
        else:
            return  
    elif request.method == 'PUT':
        user = loadUser(id)

        if(user is None):
            return jsonify({'message': 'not found'})

        user['user'] = request.json['user']
        user['password'] = encodePassword(request.json['password'])
        user['admin'] = request.json['admin']

        return jsonify({'message': 'done', 'users': user})
    elif request.method == 'DELETE':
        user = loadUser(id)

        if(user == None):
            return jsonify({'message': 'not found'})

        removeUser(user)

        return jsonify({'message': 'done', 'products': listUsers()})

@apirest.route('/users/<string:name>/<string:password>')
def authenticate(name, password):
    if auth(name, password):
        return jsonify({'message': 'done'})
    else:
        return jsonify({'message': 'error'})

@apirest.route('/users/<string:name>')
def getUserName(name):
    user = loadUserName(name)

    if(user is not None):
        return jsonify({'users': user, 'message': 'done'})
    return jsonify({'message': 'not found'})

if __name__ == '__main__':
    apirest.run(debug=True, port=5000)