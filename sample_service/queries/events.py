from pydantic import BaseModel
from datetime import date
from typing import List, Union, Optional
from queries.pool import pool


class Error(BaseModel):
    message: str


class EventIn(BaseModel):
    name: str
    date: date
    person_id: int
    occasion_id: int
    account_id: int


class EventOut(BaseModel):
    id: int
    name: str
    date: date
    person_id: int
    occasion_id: int
    account_id: int


class EventRepository:
    def update_event(
        self, event_id: int, event: EventIn
    ) -> Union[EventOut, Error]:
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
                         WHERE id = %s
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
                            event.account_id,
                            event_id,
                        ],
                    )
                    old_data = event.dict()
                    return EventOut(id=event_id, **old_data)
        except Exception as e:
            print(e)
            return {"message": "Could not update event"}

    def create_event(self, event: EventIn) -> EventOut:
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
                            event.account_id,
                        ],
                    )
                    id = db.fetchone()[0]
                    old_data = event.dict()
                    return EventOut(id=id, **old_data)
        except Exception:
            return {"message": "Could not create event"}

    def get_all(self) -> Union[Error, List[EventOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, date, person_id, occasion_id, account_id
                        FROM events
                        ORDER BY date;
                        """
                    )
                    result = []
                    for record in db:
                        event = EventOut(
                            id=record[0],
                            name=record[1],
                            date=record[2],
                            person_id=record[3],
                            occasion_id=record[4],
                            account_id=record[5],
                        )
                        result.append(event)
                    return result
        except Exception:
            return {"message": "Could not get all events"}

    def delete(self, event_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM events
                        WHERE id = %s
                        """,
                        [event_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def get_one(self, event_id: int) -> Optional[EventOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , name
                            , date,
                            , person_id
                            , occasion_id
                            , account_id
                        FROM events
                        WHERE id = %s
                        """,
                        [event_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_event_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that event"}

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
