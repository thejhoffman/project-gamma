from pydantic import BaseModel
from datetime import date
from typing import List, Union
from queries.pool import pool
from psycopg import cursor


class ErrorMessage(BaseModel):
    message: str
    code: int


class PersonOutShort(BaseModel):
    id: int
    name: str


class OccasionOutShort(BaseModel):
    id: int
    name: str


class EventIn(BaseModel):
    name: str
    date: date
    person_id: int
    occasion_id: int


class EventOut(BaseModel):
    id: int
    name: str
    date: date
    person: PersonOutShort
    occasion: OccasionOutShort


class EventRepository:
    def get_all(
        self,
        account_id: int,
    ) -> Union[List[EventOut], ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT e.id
                            , e.name
                            , e.date
                            , p.id
                            , p.name
                            , o.id
                            , o.name
                        FROM events as e
                        LEFT JOIN person as p
                        ON person_id = p.id
                        LEFT JOIN occasion as o
                        ON occasion_id = o.id
                        WHERE e.account_id = %s
                        ORDER BY date;
                        """,
                        [account_id],
                    )
                    return [
                        self.record_to_event_out(record) for record in result
                    ]
        except Exception:
            return ErrorMessage(
                message="Could not get all events",
                code=500,
            )

    def create_event(
        self,
        account_id: int,
        event: EventIn,
    ) -> Union[EventOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO events
                            (name, date, person_id, occasion_id, account_id)
                        VALUES
                            (%s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            event.name,
                            event.date,
                            event.person_id,
                            event.occasion_id,
                            account_id,
                        ],
                    )
                    id = db.fetchone()[0]
                    record = self.get_event_record(db, account_id, id)
                    return self.record_to_event_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not create event",
                code=500,
            )

    def get_one(
        self,
        account_id,
        event_id: int,
    ) -> Union[EventOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    record = self.get_event_record(db, account_id, event_id)
                    if record is None:
                        return ErrorMessage(
                            message="Event not found",
                            code=404,
                        )
                    return self.record_to_event_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not get that event",
                code=404,
            )

    def update_event(
        self,
        account_id: int,
        event_id: int,
        event: EventIn,
    ) -> Union[EventOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE events
                        SET name = %s
                            , date = %s
                            , person_id = %s
                            , occasion_id = %s
                            , account_id = %s
                        WHERE account_id = %s AND id = %s
                        RETURNING id
                                , name
                                , person_id
                                , occasion_id
                                , account_id
                        """,
                        [
                            event.name,
                            event.date,
                            event.person_id,
                            event.occasion_id,
                            account_id,
                            account_id,
                            event_id,
                        ],
                    )
                    if db.rowcount == 0:
                        return ErrorMessage(
                            message="Event not found",
                            code=404,
                        )
                    record = self.get_event_record(db, account_id, event_id)
                    return self.record_to_event_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not update event",
                code=404,
            )

    def delete(
        self,
        account_id: int,
        event_id: int,
    ) -> Union[bool, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM events
                        WHERE account_id = %s AND id = %s
                        """,
                        [account_id, event_id],
                    )
                    if db.rowcount == 0:
                        return ErrorMessage(
                            message="Event not found", code=404
                        )
                    return True
        except Exception:
            return False

    def get_event_record(self, db: cursor, account_id, event_id):
        db.execute(
            """
            SELECT e.id
                , e.name
                , e.date
                , p.id
                , p.name
                , o.id
                , o.name
                , e.account_id
            FROM events as e
            LEFT JOIN person as p
            ON person_id = p.id
            LEFT JOIN occasion as o
            ON occasion_id = o.id
            WHERE e.account_id = %s AND e.id = %s
            ORDER BY date;
            """,
            [account_id, event_id],
        )
        return db.fetchone()

    def record_to_event_out(self, record):
        return EventOut(
            id=record[0],
            name=record[1],
            date=record[2],
            person=PersonOutShort(id=record[3], name=record[4]),
            occasion=OccasionOutShort(id=record[5], name=record[6]),
        )
