from fastapi import APIRouter, Depends, Response
from typing import List, Union, Optional
from queries.events import EventIn, EventOut, EventRepository, Error
from authenticator import authenticator

router = APIRouter(tags=["Events"])


@router.post("/api/events", response_model=EventOut)
async def create_event(
    event: EventIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> EventOut:
    return repo.create_event(account_data["id"], event)


@router.get("/api/events", response_model=Union[Error, List[EventOut]])
async def get_all(
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
):
    return repo.get_all(account_data["id"])


@router.put("/api/events/{event_id}", response_model=Union[Error, EventOut])
async def update_event(
    event_id: int,
    event: EventIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[Error, EventOut]:
    return repo.update_event(account_data["id"], event_id, event)


@router.delete("/api/events/{event_id}", response_model=bool)
async def delete_event(
    event_id: int,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> bool:
    return repo.delete(event_id)


@router.get("/api/events/{event_id}", response_model= Optional[EventOut])
def get_one_event(
    event_id: int,
    response: Response,
    repo: EventRepository = Depends(),
) -> EventOut:
    event = repo.get_one(event_id)
    if event is None:
        response.status_code = 404
    return event
