import requests


def find_supreme_json():
    url = "https://www.supremenewyork.com/mobile_stock.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }


    stock = requests.get(url, headers = headers).json()

    return stock

def find_item_id(stock, category, keyword):

    for i in range(len(stock['products_and_categories'][category])):
        if keyword in stock['products_and_categories'][category][i]['name']:
            return stock['products_and_categories'][category][i]['id']
    
    print('NOT FOUND')
    return -1

def find_style_id(product_id, style, size):
    url = "https://www.supremenewyork.com/shop/" + str(product_id) + ".json"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers"
    }

    product_desc = requests.get(url, headers = headers).json()

    for i in range(len(product_desc['styles'])):
        if product_desc['styles'][i]['name'] == style:
            for j in range(len(product_desc['styles'][i]['sizes'])):
                if product_desc['styles'][i]['sizes'][j]['name'] == size:
                    return product_desc['styles'][i]['sizes'][j]['id']

    print('NOT FOUND')
    return -1

supreme_js = find_supreme_json()

jacket_id = find_item_id(supreme_js, 'Jackets', 'GORE-TEX')

add_cart_id = find_style_id(jacket_id, 'Leopard', 'XLarge')

print(add_cart_id)