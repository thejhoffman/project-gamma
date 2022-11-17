from pydantic import BaseModel
from typing import List
from queries.pool import pool


class AgeRangeIn(BaseModel):
    age: str


class AgeRangeOut(BaseModel):
    id: int
    age: str


class AgeRangeQueries:
    def get_all(self) -> List[AgeRangeOut]:
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
            return {"message": "Could get all age ranges"}

    def record_to_age_range_out(self, record):
        return AgeRangeOut(id=record[0], age=record[1])
