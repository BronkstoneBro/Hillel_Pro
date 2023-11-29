import requests

URL_CATEGORY = "https://api.escuelajs.co/api/v1/categories"
URL_GOODS = "https://api.escuelajs.co/api/v1/products"


def get_category():
    req = requests.get(URL_CATEGORY)
    print(req.status_code)
    if req.status_code == 200:
        for item in req.json():
            print(item['name'])


get_category()


def get_category_goods():
    req = requests.get(URL_GOODS)
    print(req.status_code)
    if req.status_code == 200:
        for item in req.json():
            print(item['title'])


get_category_goods()
