from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.age_range import (
    AgeRangeQueries,
    AgeRangeIn,
    AgeRangeOut,
    ErrorMessage,
)

router = APIRouter(tags=["Age Range"])


# GET ALL AGE RANGES
@router.get(
    "/api/age_range",
    response_model=Union[List[AgeRangeOut], ErrorMessage],
)
def get_all(
    repo: AgeRangeQueries = Depends(),
) -> Union[List[AgeRangeOut], ErrorMessage]:
    return repo.get_all()


# CREATE A NEW AGE RANGE
@router.post(
    "/api/age_range",
    response_model=Union[AgeRangeOut, ErrorMessage],
)
def create_age_range(
    age_range: AgeRangeIn,
    repo: AgeRangeQueries = Depends(),
) -> Union[AgeRangeOut, ErrorMessage]:
    return repo.create(age_range)


# GET DETAIL OF ONE AGE RANGE
@router.get(
    "/api/age_range/{age_range_id}",
    response_model=Union[AgeRangeOut, ErrorMessage],
)
def get_one_age_range(
    age_range_id: int,
    response: Response,
    repo: AgeRangeQueries = Depends(),
) -> Union[AgeRangeOut, ErrorMessage]:
    age_range = repo.get_one(age_range_id)
    print(age_range)
    response.status_code = set_response_code(age_range)
    return age_range


# UPDATE AN AGE RANGE
@router.put(
    "/api/age_range/{age_range_id}",
    response_model=Union[AgeRangeOut, ErrorMessage],
)
def update_age_range(
    age_range_id: int,
    age_range: AgeRangeIn,
    response: Response,
    repo: AgeRangeQueries = Depends(),
) -> Union[AgeRangeOut, ErrorMessage]:
    age_range = repo.update(age_range_id, age_range)
    response.status_code = set_response_code(age_range)
    return age_range


# DELETE AN AGE RANGE
@router.delete(
    "/api/age_range/{age_range_id}",
    response_model=Union[bool, ErrorMessage],
)
def delete_age_range(
    age_range_id: int,
    response: Response,
    repo: AgeRangeQueries = Depends(),
) -> Union[bool, ErrorMessage]:
    did_delete = repo.delete(age_range_id)
    response.status_code = set_response_code(did_delete)
    return did_delete


# function to set response code
def set_response_code(error_check):
    if type(error_check) is ErrorMessage:
        return error_check.code
