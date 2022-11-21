from fastapi import APIRouter, Depends
from typing import List, Union
from queries.events import EventIn, EventOut, EventRepository, Error

router = APIRouter(tags=["Events"])


@router.post(
    "/api/events",
    response_model=Union[EventOut, Error],
)
def create_event(event: EventIn, repo: EventRepository = Depends(),
) -> Union[EventOut, Error]:
    return repo.create_event(event)

@router.get("/api/events", response_model=Union[Error, List[EventOut]])
def get_all(
    repo: EventRepository = Depends(),
):
    return repo.get_all()

@router.put(
    "/api/events/{event_id}",
    response_model = EventOut,
)
def update_event(
    event_id: int,
    event: EventIn,
    repo: EventRepository = Depends(),
):
    event = repo.update_event(event_id, event)
    return event


@router.delete("/api/events/{event_id}", response_model=bool)
def delete_event(
    event_id: int,
    repo: EventRepository = Depends(),
 ) -> bool:
    return repo.delete(event_id)
