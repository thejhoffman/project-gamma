from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.people import PeopleQueries, PersonIn, PersonOut, ErrorMessage
from authenticator import authenticator


router = APIRouter(tags=["People"])


@router.get(
    "/api/people",
    response_model=Union[List[PersonOut], ErrorMessage],
)
async def get_all(
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: PeopleQueries = Depends(),
) -> Union[List[PersonOut], ErrorMessage]:
    return repo.get_all(account_data["id"])


@router.post(
    "/api/people",
    response_model=Union[PersonOut, ErrorMessage],
)
async def create_person(
    person: PersonIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: PeopleQueries = Depends(),
) -> Union[PersonOut, ErrorMessage]:
    return repo.create_person(account_data["id"], person)


@router.get(
    "/api/people/{person_id}",
    response_model=Union[PersonOut, ErrorMessage],
)
async def get_one_person(
    person_id: int,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: PeopleQueries = Depends(),
) -> Union[PersonOut, ErrorMessage]:
    person = repo.get_person(account_data["id"], person_id)
    response.status_code = set_response_code(person)
    return person


@router.put(
    "/api/people/{person_id}",
    response_model=Union[PersonOut, ErrorMessage],
)
async def update_person(
    person_id: int,
    person: PersonIn,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: PeopleQueries = Depends(),
) -> Union[PersonOut, ErrorMessage]:
    person = repo.update_person(account_data["id"], person_id, person)
    response.status_code = set_response_code(person)
    return person


@router.delete(
    "/api/people/{person_id}",
    response_model=Union[bool, ErrorMessage],
)
async def delete_person(
    person_id: int,
    response: Response,
    account_data: dict = Depends(authenticator.get_current_account_data),
    repo: PeopleQueries = Depends(),
) -> Union[bool, ErrorMessage]:
    did_delete = repo.delete_person(account_data["id"], person_id)
    response.status_code = set_response_code(did_delete)
    return did_delete


def set_response_code(error_check):
    if type(error_check) is ErrorMessage:
        return error_check.code
