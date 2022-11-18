from pydantic import BaseModel
from typing import List, Union
from queries.pool import pool


class ErrorMessage(BaseModel):
    message: str
    code: int


class AgeRangeIn(BaseModel):
    age: str


class AgeRangeOut(BaseModel):
    id: int
    age: str


class AgeRangeQueries:
    # GET ALL AGE RANGES
    def get_all(
        self,
    ) -> Union[List[AgeRangeOut], ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, age
                        FROM age_range
                        """
                    )
                    return [
                        self.record_to_age_range_out(record)
                        for record in result
                    ]
        except Exception:
            return ErrorMessage(
                message="Could get all age ranges",
                code=500,
            )

    # CREATE A NEW AGE RANGE
    def create(
        self,
        age_range: AgeRangeIn,
    ) -> Union[AgeRangeOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO age_range
                            (age)
                        VALUES
                            (%s)
                        RETURNING id;
                        """,
                        [age_range.age],
                    )
                    id = result.fetchone()[0]
                    return self.age_range_in_to_out(id, age_range)
        except Exception:
            return ErrorMessage(
                message="Create did not work",
                code=500,
            )

    # GET DETAIL OF ONE AGE RANGE
    def get_one(
        self,
        age_range_id: int,
    ) -> Union[AgeRangeOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, age
                        FROM age_range
                        WHERE id = %s
                        """,
                        [age_range_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return ErrorMessage(
                            message="Age range not found",
                            code=404,
                        )
                    return self.record_to_age_range_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not get that age range",
                code=500,
            )

    # UPDATE AN AGE RANGE
    def update(
        self,
        age_range_id: int,
        age_range: AgeRangeIn,
    ) -> Union[AgeRangeOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE age_range
                        SET age = %s
                        WHERE id = %s
                        """,
                        [age_range.age, age_range_id],
                    )
                    if result.rowcount == 0:
                        return ErrorMessage(
                            message="Age range not found",
                            code=404,
                        )
                    return self.age_range_in_to_out(age_range_id, age_range)
        except Exception:
            return ErrorMessage(
                message="Could not update that age range",
                code=500,
            )

    # DELETE AN AGE RANGE
    def delete(
        self,
        age_range_id: int,
    ) -> Union[bool, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        DELETE FROM age_range
                        WHERE id = %s
                        """,
                        [age_range_id],
                    )
                    if result.rowcount == 0:
                        return ErrorMessage(
                            message="Age range not found",
                            code=404,
                        )
                    return True
        except Exception:
            return False

    def age_range_in_to_out(self, id: int, age_range: AgeRangeIn):
        old_data = age_range.dict()
        return AgeRangeOut(id=id, **old_data)

    def record_to_age_range_out(self, record):
        return AgeRangeOut(id=record[0], age=record[1])
