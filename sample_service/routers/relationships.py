from fastapi import APIRouter, Depends, Response
from typing import List
from queries.relationships import (
    RelationshipIn,
    RelationshipOut,
    RelationshipRepository,
)


router = APIRouter()


@router.get(
    "/api/relationships",
    response_model=List[RelationshipOut],
    tags=["relationships"],
)
def get_all(
    repo: RelationshipRepository = Depends(),
):
    return repo.get_all()


@router.get(
    "/api/relationships/{relationship_id}",
    response_model=RelationshipOut,
    tags=["relationships"],
)
def get_relationship(
    relationship_id: int,
    response: Response,
    repo: RelationshipRepository = Depends(),
):
    relationship = repo.get_relationship(relationship_id)
    if relationship is None:
        response.status_code = 404
    return relationship


@router.post(
    "/api/relationships",
    response_model=RelationshipOut,
    tags=["relationships"],
)
def create_relationship(
    relationship: RelationshipIn,
    repo: RelationshipRepository = Depends(),
):
    return repo.create_relationship(relationship)


@router.put(
    "/api/relationships/{relationship_id}",
    response_model=RelationshipOut,
    tags=["relationships"],
)
def update_relationship(
    relationship_id: int,
    relationship: RelationshipIn,
    response: Response,
    repo: RelationshipRepository = Depends(),
):
    relationship = repo.update_relationship(relationship_id, relationship)
    if relationship is None:
        response.status_code = 404
    return relationship


@router.delete(
    "/api/relationships/{relationship_id}",
    response_model=bool,
    tags=["relationships"],
)
def delete_relationship(
    relationship_id: int,
    repo: RelationshipRepository = Depends(),
):
    return repo.delete_relationship(relationship_id)
