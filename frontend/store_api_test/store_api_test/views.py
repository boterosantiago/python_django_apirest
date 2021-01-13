from django.shortcuts import render, redirect
import requests
import json

userLogged = None
url = 'http://localhost:5000/'

def not_found_404(request, exception):
    return render(request, 'not_found.html')

def home(request):
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


def products(request):
    global userLogged
    warning = ''
    if userLogged == None:
        try:
            if(request.GET["txtUserName"] != '' and request.GET["txtPassword"] != ''):
                result = requests.get(url+'users/'+request.GET["txtUserName"]+'/'+request.GET["txtPassword"])
        except:
            result = None

        if result is not None:
            message = json.loads(result.text)['message']
            if message == 'done':
                userLogged = request.GET["txtUserName"]
                template = 'productsManager.html'
                return redirect('/products')
            else:
                template = 'login.html'
                userLogged = None
                warning = 'Wrong username or password.'
        else:
            template = 'login.html'
            userLogged = None
    else:
        template = 'productsManager.html'

    return render(request, template, {'username': userLogged, 'message': warning})

def register(request):
    warning = ''
    try:
        user = request.GET["txtUserName"]
        password = request.GET["txtPassword"]
        password2 = request.GET["txtPassword2"]

        if password != '' and user != '':
            if password == password2:
                result = requests.get(url+'users/'+user)
                if result is not None:
                    if json.loads(result.text)['message'] == 'not found':
                        new_user = {'user': user,
                        'password': password,
                        'admin': False}
                        requests.post(url+'users', json=new_user)
                        return redirect('/products')
                    else:
                        warning = 'This username already exist.'
            else:
                warning = "The passwords are different."
        else:
            warning = 'Please fill in all the data.'
    except:
        pass

    return render(request, 'register.html', {'message': warning})

'''
'code': 1,
'user': 'admin',
'password': '78b0fb9876ff57129ea2e2c49a1b93d4f8c676c43d89b7c06c2ad4188acafcab',
'admin': True
'''