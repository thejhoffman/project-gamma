from fastapi import APIRouter, Depends
from typing import Union
from queries.products import Product, ProductRepo



router = APIRouter(tags=["Products"])

@router.get("/api/products", response_model=Product)
def get_products(
    limit: int = 4,
    max_price: int = None,
    offset: int = None,
    occasion: Union[str, None] = None,
    taxonomy_id: int = None,
    gender: Union[str, None] = None,
    relationship: Union[str, None] = None,
    repo: ProductRepo = Depends(),
):
    response = repo.get_product(limit, max_price, offset, occasion, taxonomy_id, gender, relationship)
    return response
