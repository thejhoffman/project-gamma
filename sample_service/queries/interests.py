from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

class InterestsIn(BaseModel):
    name: str

class InterestsOut(BaseModel):
    id: int
    name: str

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
                    interest.name
                ]
                )
                id=result.fetchone()[0]
                old_data=interest.dict()
                return InterestsOut(id=id, **old_data)
    def get_all(self) -> Union[Error, List[InterestsOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name
                        FROM interests
                        ORDER BY id;
                        """
                    )
                    result=[]
                    for record in db:
                        interest=InterestsOut(
                            id=record[0],
                            name=record[1],
                        )
                        result.append(interest)
                    return result
        except Exception:
            return {"message": "Could not get all interests"}
