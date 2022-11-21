from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.interests import (
    InterestsIn,
    InterestsOut,
    InterestsRepository,
    Error,
)

router = APIRouter(tags=["Interests"])


@router.post("/api/interests", response_model=InterestsOut)
def create_interests(
    interest: InterestsIn,
    repo: InterestsRepository = Depends()
):
    return repo.create(interest)

@router.get("/api/interests", response_model=Union[Error, List[InterestsOut]])
def get_all(
    repo: InterestsRepository = Depends(),
):
    return repo.get_all()
