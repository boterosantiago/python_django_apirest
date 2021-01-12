from django.shortcuts import render
import requests, json

url = 'http://localhost:5000/'


def home(request):
    result = requests.get(url+'ping')

    if result.text == 'pong':
        status = 'Connected'
    else:
        status = 'Disconnected'

    return render(request, 'home.html', {
        'status': status,
        'result': result.text,
    })

def products(request):
    try:
        if(request.GET["txtName"] == ''):
            result = requests.get(url+'products')
        else:
            result = requests.get(url+'products/'+request.GET["txtName"])
    except:
        result = requests.get(url+'products')

    productsjson = json.loads(result.text)['products']
    products = []

    for j in productsjson:
        products.append(j)


    try:
        return render(request, "products.html", {'products': products, 'results': len(products)})
    except:
        return render(request, "products.html", {'products': result.text, "results": 0})