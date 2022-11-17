keys = ['name', 'productUrl', 'originalPrice', 'price', 'discount', 'ratingScore',
        'review' , 'description', 'brandName', 'sellerName']

def get_products(data):
    products = []
    for item in data['mods']['listItems']:
        products.append({
            key: item.get(key, None) for key in keys
        })
    return products