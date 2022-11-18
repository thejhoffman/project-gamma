from pydantic import BaseModel
from typing import Optional, List
from queries.pool import pool


class InterestsIn(BaseModel):
    interests: Optional[str]

class InterestsOut(BaseModel):
    id: int
    interests: Optional[str]

class InterestsRepository(BaseModel):
    def create(self, interest: InterestsIn) -> InterestsOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result=db.execute(
                    """
                    INSERT INTO interests
                        (name)
                    VALUES
                        (%s)
                    RETURNING id;
                    """,
                [
                    interest.interests
                ]
                )
                id=result.fetchone()[0]
                old_data=interest.dict()
                return InterestsOut(id=id, **old_data)
