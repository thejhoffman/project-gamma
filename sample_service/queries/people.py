from pydantic import BaseModel
from typing import List, Union, Optional
from queries.pool import pool


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
    age_range_id: int
    gender_id: Optional[int]
    # account_id: int
    interest_id: int
    relationship_id: int


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
                        SELECT
                            id
                            , name
                            , age_range_id
                            , gender_id
                            , account_id
                            , interest_id
                            , relationship_id
                        FROM person
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
                    return self.person_in_to_out(id, person)
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
                    db.execute(
                        """
                        SELECT id
                            , name
                            , age_range_id
                            , gender_id
                            , account_id
                            , interest_id
                            , relationship_id
                        FROM person
                        WHERE account_id = %s AND id = %s
                        """,
                        [account_id, person_id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return ErrorMessage(
                            message="Person not found",
                            code=404,
                        )
                    return self.record_to_person_out(record)
        except Exception:
            return ErrorMessage(
                message="Could not get that person",
                code=404,
            )

    # UPDATE A PERSON
    def update_person(
        self,
        account_id: int,
        person_id,
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
                    return self.person_in_to_out(person_id, person)
        except Exception:
            return ErrorMessage(
                message="Could not update person",
                code=404,
            )

    # DELETE A PERSON
    def delete_person(
        self,
        account_id: int,
        person_id,
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
    def person_in_to_out(self, id: int, person: PersonIn):
        old_data = person.dict()
        return PersonOut(id=id, **old_data)

    def record_to_person_out(self, record):
        return PersonOut(
            id=record[0],
            name=record[1],
            age_range_id=record[2],
            gender_id=record[3],
            account_id=record[4],
            interest_id=record[5],
            relationship_id=record[6],
        )
