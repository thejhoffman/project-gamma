import json
import requests
from pydantic import BaseModel
import os

ETSY_API_KEY = os.environ["ETSY_API_KEY"]

class Product(BaseModel):
    products: list

class ProductRepo:
    def get_product(self, interest, occasion, gender, relationship, max_price):
        params = {
            "api_key": ETSY_API_KEY,
            "limit": 4,
            "method": "GET",
            "fields": "title,description,url,price",
            "includes": "MainImage",
            "keywords": f"${interest},${occasion},${gender},${relationship}",
            "max_price": {max_price}
            }
        url = "https://openapi.etsy.com/v2/listings/active?"

        response = requests.get(url, params=params)
        content = json.loads(response.content)

        products = []
        for item in content["results"]:
            products.append(item)

        try:
            return {"products": products}
        except (KeyError, IndexError):
            return {"title": None}
