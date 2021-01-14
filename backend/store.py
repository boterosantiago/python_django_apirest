products = [
    {
        'url': "https://images.samsung.com/co/smartphones/galaxy-note20/buy/001-note20series-productimage-mo-720.jpg",
        'code': 1,
        "name": 'samsung',
        'description': '''cpu: 2GHz
        ram: 2Gb
        camera: 13mp''',
        'price': 600000,
        'stock': 200
    },
    {
        'url': "https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/_/0/_0002_8806087043716-06.jpg",
        'code': 2,
        "name": 'lg',
        'description': '''cpu: 1GHz
        ram: 4Gb
        camera: 8mp''',
        'price': 400000,
        'stock': 50
    },
    {
        'url': "https://fontalvocell.com/wp-content/uploads/2019/08/nokia_106_gray.png",
        'code': 3,
        "name": 'nokia',
        'description': '''cpu: 20GHz
        ram: 24Gb
        camera: 64mp''',
        'price': 100000,
        'stock': 20
    },
    {
        'url': "https://doto.vteximg.com.br/arquivos/ids/157127-1200-1200/realme_00_realme6-azul-dotomexico-bothview.jpg?v=637238840643170000",
        'code': 4,
        "name": 'realme',
        'description': '''cpu: 2GHz
        ram: 4Gb
        camera: 64mp''',
        'price': 700000,
        'stock': 5
    },
    {
        'url': "https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/6/9/6941059646785_004.jpg",
        'code': 5,
        "name": 'xiaomi',
        'description': '''cpu: 2GHz
        ram: 8Gb
        camera: 48mp''',
        'price': 1000000,
        'stock': 150
    },
    {
        'url': "https://media.aws.alkosto.com/media/catalog/product/cache/6/image/69ace863370f34bdf190e4e164b6e123/6/9/6901443366187_1.jpg",
        'code': 6,
        "name": 'huahuey',
        'description': '''cpu: 1GHz
        ram: 4Gb
        camera: 13mp''',
        'price': 600000,
        'stock': 5
    },
    {
        'url': "https://media.revistagq.com/photos/5ed4bdebf95b900ced636e00/master/pass/iphone13.jpg",
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