import json
import requests
from pydantic import BaseModel
import os

ETSY_API_KEY = os.environ["ETSY_API_KEY"]

class Product(BaseModel):
    products: list

class ProductRepo:
    def get_product(self, max_price, offset, occasion, taxonomy_id, gender, relationship):
        params = {
                "api_key": ETSY_API_KEY,
                "limit": 4,
                "method": "GET",
                "fields": "title,description,url,price",
                "includes": "MainImage",
            }
        if max_price != None and "None":
            params["max_price"] = max_price
        if offset != None and "None":
            params["offset"] = offset
        if taxonomy_id != None and "None":
            params["taxonomy_id"] = taxonomy_id
        keywords = []
        if occasion != None:
            keywords.append(occasion)
        if gender != None:
            keywords.append(gender)
        if relationship != None:
            keywords.append(relationship)
        if len(keywords) != 0:
            params["keywords"] = ",".join(keywords)

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
