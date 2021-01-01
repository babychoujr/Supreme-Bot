import requests

#find the json file from supreme
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

#finds the product wanted from supreme json based on 
#category: ie. 'Jackets'...
#keyword: keyword to find the product_id
def find_item_id(stock, category, keyword):

    for i in range(len(stock['products_and_categories'][category])):
        if keyword in stock['products_and_categories'][category][i]['name']:
            return stock['products_and_categories'][category][i]['id']
    
    print('NOT FOUND')
    return -1


def find_style_id(product_id, style):
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
            return product_desc['styles'][i]['id']
    
    print('NOT FOUND')
    return -1

#navigates to the product endpoint json file
#finds the product_id of the product based on style and size for the specific item
def find_size_id(product_id, style, size):
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

#add_cart - 
def add_cart(product_id, style_id, size_id):
    #add_cart link
    url = "https://www.supremenewyork.com/shop/" + str(product_id) + "/add.json"

    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",
        "Connection": "close",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "Trailers",
        "content-type": "application/x-www-form-urlencoded"
    }

    data = {
        "s":size_id,
        "st":style_id,
        "qty": "1"
    }

    add_cart = requests.post(url, headers = headers, data = data).json()

    return add_cart


supreme_js = find_supreme_json()

item_id = find_item_id(supreme_js, 'Jackets', 'GORE-TEX')

style_id = find_style_id(item_id, 'Light Olive')

size_id = find_size_id(item_id, 'Light Olive', 'Large')

print("ITEM_ID: ", item_id)
print("STYLE_ID: ", style_id)
print("SIZE_ID: ", size_id)

print(add_cart(item_id, style_id, size_id))