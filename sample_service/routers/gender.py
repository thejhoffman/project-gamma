from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.gender import (
    Error,
    GenderIn,
    GenderRepository,
    GenderOut,
)


router = APIRouter(tags=["Gender"])


@router.post("/gender", response_model=Union[GenderOut, Error])
def create_gender(
    gender: GenderIn,
    response: Response,
    repo: GenderRepository = Depends(),
):
    response.status_code = 400
    return repo.create(gender)


@router.get("/gender", response_model=Union[Error, List[GenderOut]])
def get_all(
    repo: GenderRepository = Depends(),
):
    return repo.get_all()
