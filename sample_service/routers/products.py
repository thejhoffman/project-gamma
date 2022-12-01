from fastapi import APIRouter, Depends
from typing import Union
from queries.products import Product, ProductRepo



router = APIRouter(tags=["Products"])

@router.get("/api/products", response_model=Product)
def get_products(
    max_price: int = None,
    offset: int = None,
    occasion: Union[str, None] = None,
    interest: Union[str, None] = None,
    gender: Union[str, None] = None,
    relationship: Union[str, None] = None,
    repo: ProductRepo = Depends(),
):
    response = repo.get_product(max_price, offset, occasion, interest, gender, relationship)
    return response
