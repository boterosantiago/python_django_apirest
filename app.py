from flask import Flask, jsonify
from store import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/products')
def getProducts():
    return jsonify({'products': products})

@app.route('/products/<int:id>')
def getProductId(id):
    product = 'not found'
    for p in products:
        if(p['code'] == id):
            product = p
            continue
    return product

@app.route('/products/<string:name>')
def getProduct(name):
    products2 = [p for p in products if p['name'].lower() == name.lower()]
    
    results = len(products2)

    if(results > 0):
        return jsonify({'products': products2, "results": results})
    return 'not found'

if __name__ == '__main__':
    app.run(debug=True, port=5000)