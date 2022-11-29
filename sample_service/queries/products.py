import json
import requests
# import os

# # ETSY_API_KEY = os.environ["ETSY_API_KEY"]

# def get_product():
#     params = {
#         # "max_price": "100",
#         # "includes": "images",
#         # "taxonomy_id": "1432",
#         # "keywords": f"{interest}",
#         "api_key": "o2y8damjweefvmlsytbbz2fm"
#     }
#     url = "https://api.etsy.com/v3/application/openapi-ping"
#     response = requests.get(url, params=params)
#     print(response)
#     content = json.loads(response.content)

#     try:
#         return {"product_info": content["count"]}
#     except (KeyError,IndexError):
#         return {"product_info": "cannot get product"}


from pydantic import BaseModel
import os
from typing import Optional

ETSY_API_KEY = os.environ["ETSY_API_KEY"]

class Product(BaseModel):
    products: list

class ProductRepo:
    def get_product(self, interest, max_price):
        params = {
            "api_key": ETSY_API_KEY,
            "limit": 4,
            "includes": "images",
            "keywords": {interest},
            "max_price": {max_price}
            }
        url = "https://openapi.etsy.com/v2/listings/active?"

        response = requests.get(url, params=params)
        content = json.loads(response.content)
        print(content)

        products = []
        for item in content["results"]:
            products.append(item)

        try:
            return {"products": products}
        except (KeyError, IndexError):
            return {"title": None}
