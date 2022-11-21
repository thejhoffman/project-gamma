from fastapi import APIRouter, Depends
from typing import List, Union
from queries.events import EventIn, EventOut, EventRepository, Error

router = APIRouter(tags=["Events"])


@router.post("/api/events", tags=["events"])
def create_event(event: EventIn):
    print("event", event)
    return event
