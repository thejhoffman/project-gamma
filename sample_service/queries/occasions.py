from pydantic import BaseModel
from typing import List
from queries.pool import pool
from datetime import date


class OccasionIn(BaseModel):
    name: str
    date: date


class OccasionOut(BaseModel):
    id: int
    name: str
    date: date


class OccasionRepository:
    def get_all(self) -> List[OccasionOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name, date
                        FROM occasion
                        ORDER BY date;
                        """
                    )
                    return [
                        OccasionOut(
                            id=record[0], name=record[1], date=record[2]
                        )
                        for record in db
                    ]
        except Exception:
            return {"message": "could not get all occasions"}

    def get_occasion(self, occasion_id: int) -> OccasionOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, name, date
                        FROM occasion
                        WHERE id = %s
                        """,
                        [occasion_id],
                    )
                    row = db.fetchone()
                    return OccasionOut(id=row[0], name=row[1], date=row[2])
        except Exception:
            return {"message": "could not get occasion"}

    def create_occasion(self, occasion: OccasionIn) -> OccasionOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO occasion (name, date)
                        VALUES (%s, %s)
                        RETURNING id;
                        """,
                        [occasion.name, occasion.date],
                    )
                    id = db.fetchone()[0]
                    old_data = occasion.dict()
                    return OccasionOut(id=id, **old_data)
        except Exception:
            return {"message": "could not create occasion"}

    def update_occasion(
        self, occasion_id, occasion: OccasionIn
    ) -> OccasionOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE occasion
                        SET name = %s
                            , date = %s
                        WHERE id = %s
                        RETURNING id, name, date
                        """,
                        [occasion.name, occasion.date, occasion_id],
                    )
                    record = None
                    row = db.fetchone()
                    if row is not None:
                        record = {}
                        for i, column in enumerate(db.description):
                            record[column.name] = row[i]

                    return record
        except Exception:
            return {"message": "could not update occasion"}

    def delete_occasion(self, occasion_id) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from occasion
                        WHERE id = %s
                        """,
                        [occasion_id],
                    )
                    return True
        except Exception:
            return False
