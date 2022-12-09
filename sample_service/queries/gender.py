from pydantic import BaseModel
from typing import Union, List
from queries.pool import pool


class Error(BaseModel):
    message: str


class GenderIn(BaseModel):
    name: str


class GenderOut(BaseModel):
    id: int
    name: str


class GenderRepository:
    def get_all(self) -> Union[Error, List[GenderOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name
                        FROM gender
                        ORDER BY id;
                        """
                    )
                    result = []
                    for record in db:
                        gender = GenderOut(id=record[0], name=record[1])
                        result.append(gender)
                    return result

        except Exception:
            return {"message": "Could not get gender"}

    def create(self, gender: GenderIn) -> GenderOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                    INSERT INTO gender
                        (name)
                    VALUES
                        (%s)
                    RETURNING id;
                    """,
                    [gender.name],
                )
                id = result.fetchone()[0]
                old_data = gender.dict()
                return GenderOut(id=id, **old_data)
