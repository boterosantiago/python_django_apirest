from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import requests
import json
import datetime

userLogged = None
url = 'http://localhost:5000/'

def not_found_404(request, exception):
    return render(request, 'not_found.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

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

def product_detail(request, code):
    product = None
    try:
        result = requests.get(url+'products/'+str(code))
        if result is not None:
            if json.loads(result.text)['message'] == 'Done':
                product = json.loads(result.text)['product']
    except:
        pass

    return render(request, 'product_detail.html', {'product': product, 'rows': len(product['description'].split("\n"))})

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
                return redirect('/register_product')
            else:
                userLogged = None
                warning = 'Wrong username or password.'
        else:
            userLogged = None
    else:
        return redirect('/register_product')

    return render(request, 'login.html', {'username': userLogged, 'message': warning})

def register_product(request):
    try:
        name = request.GET["txtName"] # required
        desc = request.GET["txtDesc"]
        price = request.GET["txtPrice"] # required
        stock = request.GET["txtStock"] # required

        if name == '' or desc == '' or price == '' or stock == '': # or urls == '':
            message = 'Please fill in all the data.'
        else:
            # Upload system https://www.youtube.com/watch?v=Zx09vcYq1oc
            #date1 = datetime.datetime.now()
            #date = str(date1.year)+"-"+str(date1.month)+"-"+str(date1.day)
            #message = '1'
            #uploaded_file = request.FILEs['images_uploader']
            #message = '2'
            #fs = FileSystemStorage()
            #message = '3'
            #url = fs.url(fs.save(uploaded_file.name + date, uploaded_file))
            #message = '4'

            new_product = {'name': name,
            'description': desc,
            'price': price,
            'stock': stock}
            requests.post(url+'products', json=new_product)
            message = "Done!"
    except:
        message = ''

    return render(request, 'products_manager.html', {'message': message})

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
