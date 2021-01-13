products = [
    {
        'code': 1,
        "name": 'samsung',
        'description': '''cpu: 2GHz
        ram: 2Gb
        camera: 13mp''',
        'price': 600000,
        'stock': 200
    },
    {
        'code': 2,
        "name": 'lg',
        'description': '''cpu: 1GHz
        ram: 4Gb
        camera: 8mp''',
        'price': 400000,
        'stock': 50
    },
    {
        'code': 3,
        "name": 'nokia',
        'description': '''cpu: 20GHz
        ram: 24Gb
        camera: 64mp''',
        'price': 100000,
        'stock': 20
    },
    {
        'code': 4,
        "name": 'realme',
        'description': '''cpu: 2GHz
        ram: 4Gb
        camera: 64mp''',
        'price': 700000,
        'stock': 5
    },
    {
        'code': 5,
        "name": 'xiaomi',
        'description': '''cpu: 2GHz
        ram: 8Gb
        camera: 48mp''',
        'price': 1000000,
        'stock': 150
    },
    {
        'code': 6,
        "name": 'huawei',
        'description': '''cpu: 1GHz
        ram: 4Gb
        camera: 13mp''',
        'price': 600000,
        'stock': 5
    },
    {
        'code': 7,
        "name": 'iphone',
        'description': '''cpu: 1GHz
        ram: 1Gb
        camera: 2mp
        
        A very expensive and useless cellphone''',
        'price': 6000000,
        'stock': 2000
    },
    
]

def product_auto_code():
    code = 1
    exist = True
    while exist:
        exist = False
        for p in products:
            if p['code'] == code:
                exist = True
                code += 1
                break
    return code