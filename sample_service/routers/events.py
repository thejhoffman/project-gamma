from fastapi import APIRouter, Depends
from typing import List, Union
from queries.events import EventIn, EventOut, EventRepository, Error

router = APIRouter(tags=["Events"])


@router.post("/api/events", response_model=EventOut, tags=["events"])
def create_event(event: EventIn):
    event: EventIn
    repo: EventRepository = Depends()
    return repo.create(event)


@router.get("/api/events", response_model=Union[Error, List[EventOut]])
def get_all(
    repo: EventOut = Depends(),
):
    return repo.get_all()


# @router.get("/api/events/")
