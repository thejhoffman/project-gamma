from pydantic import BaseModel
from datetime import date
from typing import List, Union
from queries.pool import pool

class Error(BaseModel):
    message:str

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
    def create_event(self, event:EventIn) -> EventOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
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
                            event.account_id
                        ]
                        )
                    id=result.fetchone()[0]
                    old_data=event.dict()
                    return EventOut(id=id, **old_data)
        except Exception:
            return {"message": "Could not create event"}


    def get_all(self): -> Union[Error, List[EventOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT name, date, person_id, occiasion_id, account_id
                        FROM Events
                        ORDER BY date;
                        """
                    )
                    result = []
                    for record in db:
                        event = EventOut(
                            name=record[0],
                            date=record[1],
                            person_id=record[2],
                            occasion_id=record[3],
                            account_id=record[4],
                        )
                        result.append(event)
                    return result
        except Exception:
            return {"message": "Could not get all events"}
