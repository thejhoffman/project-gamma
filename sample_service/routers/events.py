from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.events import EventIn, EventOut, EventRepository, Error

router = APIRouter(tags=["Events"])


@router.post("/api/events", response_model=EventOut, tags=["events"])
def create_event(
    event: EventIn, repo: EventRepository = Depends()
) -> EventOut:
    return repo.create_event(event)


@router.get("/api/events", response_model=Union[Error, List[EventOut]])
def get_all(
    repo: EventRepository = Depends(),
):
    return repo.get_all()


@router.put("/api/events/{event_id}", response_model=Union[Error, EventOut])
def update_event(
    event_id: int,
    event: EventIn,
    repo: EventRepository = Depends(),
) -> Union[Error, EventOut]:
    return repo.update_event(event_id, event)


@router.delete("/api/events/{event_id}", response_model=bool)
def delete_event(
    event_id: int,
    repo: EventRepository = Depends(),
) -> bool:
    return repo.delete(event_id)
