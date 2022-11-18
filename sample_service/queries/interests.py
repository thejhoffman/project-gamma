from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class InterestsIn(BaseModel):
    interests: Optional[str]

class InterestsRepository(BaseModel):
    def create(interest: InterestsIn):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result=db.execute(
                    """
                   INSERT INTO events
                    (interests)
                    VALUES
                    (%s);
                    """
                [
                    interest.interests
                ]
                )
