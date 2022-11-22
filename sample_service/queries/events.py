from pydantic import BaseModel
from datetime import date
from typing import List, Union
from queries.pool import pool


class ErrorMessage(BaseModel):
    message: str
    code: int


class EventIn(BaseModel):
    name: str
    date: date
    person_id: int
    occasion_id: int


class EventOut(BaseModel):
    id: int
    name: str
    date: date
    person_id: int
    occasion_id: int


class EventRepository:
    # GET ALL EVENTS
    def get_all(
        self,
        account_id: int,
    ) -> Union[List[EventOut], ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , name
                            , date
                            , person_id
                            , occasion_id
                            , account_id
                        FROM events
                        WHERE account_id = %s
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

    #  CREATE A NEW PERSON
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
                    return self.event_in_to_out(id, event)
        except Exception:
            return ErrorMessage(
                message="Could not create event",
                code=500,
            )

    # GET DETAIL OF ONE EVENT
    def get_one(
        self,
        account_id,
        event_id: int,
    ) -> Union[EventOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , name
                            , date
                            , person_id
                            , occasion_id
                            , account_id
                        FROM events
                        WHERE account_id = %s AND id = %s
                        """,
                        [account_id, event_id],
                    )
                    record = result.fetchone()
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

    # UPDATE AN EVENT
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
                    return self.event_in_to_out(event_id, event)
        except Exception:
            return ErrorMessage(
                message="Could not update event",
                code=404,
            )

    # DELETE AN EVENT
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

    # helper methods
    def event_in_to_out(self, id: int, event: EventIn):
        old_data = event.dict()
        return EventOut(id=id, **old_data)

    def record_to_event_out(self, record):
        return EventOut(
            id=record[0],
            name=record[1],
            date=record[2],
            person_id=record[3],
            occasion_id=record[4],
            account_id=record[5],
        )
