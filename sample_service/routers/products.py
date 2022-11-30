from fastapi import APIRouter, Depends
from typing import Union
from queries.products import Product, ProductRepo



router = APIRouter(tags=["Products"])

@router.get("/api/products", response_model=Product)
def get_products(
    interest: Union[str, None] = None,
    occasion: Union[str, None] = None,
    gender: Union[str, None] = None,
    relationship: Union[str, None] = None,
    max_price: Union[str, None] = None,
    repo: ProductRepo = Depends(),
):
    response = repo.get_product(interest, occasion, gender, relationship, max_price)
    return response
