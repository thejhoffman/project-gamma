from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.interests import (
    InterestsIn,
    InterestsRepository,
)

router = APIRouter()


@router.post("/api/interests")
def create_interests(
    interest: InterestsIn,
    repo: InterestsRepository = Depends()
):
    return interest
