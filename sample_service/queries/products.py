import json
import requests
from pydantic import BaseModel
import os

ETSY_API_KEY = os.environ["ETSY_API_KEY"]


class Product(BaseModel):
    products: list


class ProductRepo:
    def get_product(
        self,
        limit,
        max_price,
        offset,
        occasion,
        taxonomy_id,
        gender,
        relationship,
    ):
        params = {
            "api_key": ETSY_API_KEY,
            "limit": limit,
            "method": "GET",
            "fields": "title,description,url,price,currency_code",
            "includes": "MainImage",
            "sort_on": "score",
        }
        if max_price is not None and "None":
            params["max_price"] = max_price
        if offset is not None and "None":
            params["offset"] = offset
        if taxonomy_id is not None and "None":
            params["taxonomy_id"] = taxonomy_id
        keywords = []
        if occasion is not None:
            keywords.append(occasion)
        if gender is not None:
            if gender == "male":
                gender = "mens"
            elif gender == "female":
                gender = "womens"
            else:
                gender = "unisex"
            keywords.append(gender)
        if relationship is not None:
            keywords.append(relationship)
        if len(keywords) != 0:
            params["keywords"] = ",".join(keywords)

        url = "https://openapi.etsy.com/v2/listings/active?"

        response = requests.get(url, params=params)
        content = json.loads(response.content)

        print(params)

        products = []
        for item in content["results"]:
            products.append(item)

        try:
            return {"products": products}
        except (KeyError, IndexError):
            return {"title": None}
