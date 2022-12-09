from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.events import EventIn, EventOut, EventRepository, ErrorMessage
from authenticator import authenticator


router = APIRouter(tags=["Events"])


@router.get(
    "/api/events",
    response_model=Union[List[EventOut], ErrorMessage],
)
async def get_all(
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[List[EventOut], ErrorMessage]:
    return repo.get_all(account_data["id"])


@router.post(
    "/api/events",
    response_model=Union[EventOut, ErrorMessage],
)
async def create_event(
    event: EventIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[EventOut, ErrorMessage]:
    return repo.create_event(account_data["id"], event)


@router.get(
    "/api/events/{event_id}",
    response_model=Union[EventOut, ErrorMessage],
)
async def get_one_event(
    event_id: int,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[EventOut, ErrorMessage]:
    event = repo.get_one(account_data["id"], event_id)
    response.status_code = set_response_code(event)
    return event


@router.put(
    "/api/events/{event_id}",
    response_model=Union[EventOut, ErrorMessage],
)
async def update_event(
    event_id: int,
    event: EventIn,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[EventOut, ErrorMessage]:
    event = repo.update_event(account_data["id"], event_id, event)
    response.status_code = set_response_code(event)
    return event


@router.delete(
    "/api/events/{event_id}",
    response_model=Union[bool, ErrorMessage],
)
async def delete_event(
    event_id: int,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: EventRepository = Depends(),
) -> Union[bool, ErrorMessage]:
    did_delete = repo.delete(account_data["id"], event_id)
    response.status_code = set_response_code(did_delete)
    return did_delete


def set_response_code(error_check):
    if type(error_check) is ErrorMessage:
        return error_check.code
