from pydantic import BaseModel
from typing import List, Union, Optional
from queries.pool import pool
from queries.age_range import AgeRangeOut
from queries.gender import GenderOut
from queries.interests import InterestsOut
from queries.relationships import RelationshipOut
from psycopg import cursor


class ErrorMessage(BaseModel):
    message: str
    code: int


class PersonIn(BaseModel):
    name: str
    age_range_id: int
    gender_id: int
    interest_id: int
    relationship_id: int


class PersonOut(BaseModel):
    id: int
    name: str
    age_range: AgeRangeOut
    gender: Optional[GenderOut]
    interest: InterestsOut
    relationship: RelationshipOut


class PeopleQueries:
    # GET ALL PEOPLE
    def get_all(
        self,
        account_id: int,
    ) -> Union[List[PersonOut], ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT p.id
                            , p.name
                            , a.id
                            , a.age
                            , g.id
                            , g.name
                            , i.id
                            , i.name
                            , r.id
                            , r.type
                        FROM person as p
                        LEFT JOIN age_range as a
                        ON age_range_id = a.id
                        LEFT JOIN gender as g
                        ON gender_id = g.id
                        LEFT JOIN interests as i
                        ON interest_id = i.id
                        LEFT JOIN relationships as r
                        ON relationship_id = r.id
                        WHERE account_id = %s
                        """,
                        [account_id],
                    )
                    return [
                        self.record_to_person_out(record) for record in result
                    ]
        except Exception:
            return ErrorMessage(
                message="Could not get all people",
                code=500,
            )

    # CREATE A NEW PERSON
    def create_person(
        self,
        account_id: int,
        person: PersonIn,
    ) -> Union[PersonOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO person (
                            name
                            , age_range_id
                            , gender_id
                            , account_id
                            , interest_id
                            , relationship_id
                        )
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            person.name,
                            person.age_range_id,
                            person.gender_id,
                            account_id,
                            person.interest_id,
                            person.relationship_id,
                        ],
                    )
                    id = db.fetchone()[0]
                    record = self.get_person_record(db, account_id, id)
                    return self.record_to_person_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not create person",
                code=500,
            )

    # GET DETAIL OF ONE PERSON
    def get_person(
        self,
        account_id: int,
        person_id: int,
    ) -> Union[PersonOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    record = self.get_person_record(db, account_id, person_id)
                    if record is None:
                        return ErrorMessage(
                            message="Person not found",
                            code=404,
                        )
                    return self.record_to_person_out(record)
        except Exception as e:
            return ErrorMessage(
                # message="Could not get that person",
                message=str(e),
                code=404,
            )

    # UPDATE A PERSON
    def update_person(
        self,
        account_id: int,
        person_id: int,
        person: PersonIn,
    ) -> Union[PersonOut, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE person
                        SET name = %s
                            , age_range_id = %s
                            , gender_id = %s
                            , account_id = %s
                            , interest_id = %s
                            , relationship_id = %s
                        WHERE account_id = %s AND id = %s
                        RETURNING id
                                , name
                                , age_range_id
                                , gender_id
                                , account_id
                                , interest_id
                                , relationship_id
                        """,
                        [
                            person.name,
                            person.age_range_id,
                            person.gender_id,
                            account_id,
                            person.interest_id,
                            person.relationship_id,
                            account_id,
                            person_id,
                        ],
                    )
                    if db.rowcount == 0:
                        return ErrorMessage(
                            message="Person not found",
                            code=404,
                        )
                    record = self.get_person_record(db, account_id, person_id)
                    return self.record_to_person_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not update person",
                code=404,
            )

    # DELETE A PERSON
    def delete_person(
        self,
        account_id: int,
        person_id: int,
    ) -> Union[bool, ErrorMessage]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from person
                        WHERE account_id = %s AND id = %s
                        """,
                        [account_id, person_id],
                    )
                    if db.rowcount == 0:
                        return ErrorMessage(
                            message="Person not found", code=404
                        )
                    return True
        except Exception:
            return False

    # helper methods
    def get_person_record(self, db: cursor, account_id, person_id):
        db.execute(
            """
            SELECT p.id
                , p.name
                , a.id
                , a.age
                , g.id
                , g.name
                , i.id
                , i.name
                , r.id
                , r.type
            FROM person as p
            LEFT JOIN age_range as a
            ON age_range_id = a.id
            LEFT JOIN gender as g
            ON gender_id = g.id
            LEFT JOIN interests as i
            ON interest_id = i.id
            LEFT JOIN relationships as r
            ON relationship_id = r.id
            WHERE account_id = %s AND p.id = %s
            """,
            [account_id, person_id],
        )
        return db.fetchone()

    def record_to_person_out(self, record):
        return PersonOut(
            id=record[0],
            name=record[1],
            age_range=AgeRangeOut(id=record[2], age=record[3]),
            gender=GenderOut(id=record[4], name=record[5]),
            interest=InterestsOut(id=record[6], name=record[7]),
            relationship=RelationshipOut(id=record[8], type=record[9]),
        )
