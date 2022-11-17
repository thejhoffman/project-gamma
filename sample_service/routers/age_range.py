from fastapi import APIRouter, Depends
from typing import List
from queries.age_range import AgeRangeQueries, AgeRangeOut

router = APIRouter(tags=["Age Range"])


@router.get("/api/age_range", response_model=List[AgeRangeOut])
def get_all(repo: AgeRangeQueries = Depends()):
    return repo.get_all()
