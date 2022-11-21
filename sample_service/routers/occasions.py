from fastapi import APIRouter, Depends, Response
from typing import List
from queries.occasions import OccasionIn, OccasionOut, OccasionRepository

router = APIRouter(tags=["Occasions"])


@router.get("/api/occasions", response_model=List[OccasionOut])
def get_all(
    repo: OccasionRepository = Depends(),
):
    return repo.get_all()


@router.get(
    "/api/occasions/{occasion_id}",
    response_model=OccasionOut,
)
def get_occasion(
    occasion_id: int,
    response: Response,
    repo: OccasionRepository = Depends(),
):
    occasion = repo.get_occasion(occasion_id)
    if occasion is None:
        response.status_code = 404
    return occasion


@router.post("/api/occasions", response_model=OccasionOut)
def create_occasion(
    occasion: OccasionIn,
    repo: OccasionRepository = Depends(),
):
    return repo.create_occasion(occasion)


@router.put(
    "/api/occasions/{occasion_id}",
    response_model=OccasionOut,
)
def update_occasion(
    occasion_id: int,
    occasion: OccasionIn,
    response: Response,
    repo: OccasionRepository = Depends(),
):
    occasion = repo.update_occasion(occasion_id, occasion)
    if occasion is None:
        response.status_code = 404
    return occasion


@router.delete(
    "/api/occasions/{occasion_id}",
    response_model=bool,
)
def delete_occasion(
    occasion_id: int,
    repo: OccasionRepository = Depends(),
):
    return repo.delete_occasion(occasion_id)
