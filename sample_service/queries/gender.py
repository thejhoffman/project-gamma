from pydantic import BaseModel
from typing import Union, List, Optional
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
            # connect the database
            with pool.connection() as conn:
                # get cursor
                with conn.cursor() as db:
                    # Run our SELECT statement
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
        # connect the database
        with pool.connection() as conn:
            # get cursor
            with conn.cursor() as db:
                # run our INSERT
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
                # Return new data
                old_data = gender.dict()
                return GenderOut(id=id, **old_data)
