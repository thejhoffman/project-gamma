from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.people import PeopleQueries, PersonIn, PersonOut, ErrorMessage


router = APIRouter(tags=["People"])


# GET ALL PEOPLE
@router.get(
    "/api/people",
    response_model=Union[List[PersonOut], ErrorMessage],
)
def get_all(
    repo: PeopleQueries = Depends(),
) -> Union[List[PersonOut], ErrorMessage]:
    return repo.get_all()


# CREATE A NEW PERSON
@router.post(
    "/api/people",
    response_model=Union[List[PersonOut], ErrorMessage],
)
def create_person(
    person: PersonIn,
    repo: PeopleQueries = Depends(),
) -> Union[List[PersonOut], ErrorMessage]:
    return repo.create_person(person)


# GET DETAIL OF ONE PERSON
@router.get(
    "/api/people/{person_id}",
    response_model=Union[PersonOut, ErrorMessage],
)
def get_one_person(
    person_id: int,
    response: Response,
    repo: PeopleQueries = Depends(),
) -> Union[PersonOut, ErrorMessage]:
    person = repo.get_person()(person_id)
    response.status_code = set_response_code(person)
    return person


# UPDATE A PERSON
@router.put(
    "/api/people/{person_id}",
    response_model=Union[PersonOut, ErrorMessage],
)
def update_person(
    person_id: int,
    person: PersonIn,
    response: Response,
    repo: PeopleQueries = Depends(),
) -> Union[PersonOut, ErrorMessage]:
    person = repo.update_person()(person_id, person)
    response.status_code = set_response_code(person)
    return person


# DELETE A PERSON
@router.delete(
    "/api/people/{person_id}",
    response_model=Union[bool, ErrorMessage],
)
def delete_person(
    person_id: int,
    response: Response,
    repo: PeopleQueries = Depends(),
) -> Union[bool, ErrorMessage]:
    did_delete = repo.delete(person_id)
    response.status_code = set_response_code(did_delete)
    return did_delete


# function to set response code
def set_response_code(error_check):
    if type(error_check) is ErrorMessage:
        return error_check.code
