from pydantic import BaseModel
from typing import List
from queries.pool import pool


class RelationshipIn(BaseModel):
    type: str


class RelationshipOut(BaseModel):
    id: int
    type: str


class RelationshipRepository:
    def get_all(self) -> List[RelationshipOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, type
                        FROM relationships
                        ORDER BY type;
                        """
                    )
                    return [
                        RelationshipOut(id=record[0], type=record[1])
                        for record in db
                    ]
        except Exception as e:
            print(e)
            return {" message": "could not get all vacations"}

    def get_relationship(self, relationship_id: int) -> RelationshipOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, type
                        FROM relationships
                        WHERE id = %s
                        """,
                        [relationship_id],
                    )
                    row = db.fetchone()
                    return RelationshipOut(id=row[0], type=row[1])
        except Exception:
            return {"message": "could not get that relationship"}

    def create_relationship(
        self, relationship: RelationshipIn
    ) -> RelationshipOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO relationships (type)
                        VALUES (%s)
                        RETURNING id
                        """,
                        [relationship.type],
                    )
                    id = db.fetchone()[0]
                    old_data = relationship.dict()
                    return RelationshipOut(id=id, **old_data)
        except Exception:
            return {"message": "could not create relationship"}

    def update_relationship(
        self, relationship_id, relationship: RelationshipIn
    ) -> RelationshipOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE relationships
                        SET type = %s
                        WHERE id = %s
                        RETURNING id, type
                        """,
                        [relationship.type, relationship_id],
                    )
                    record = None
                    row = db.fetchone()
                    if row is not None:
                        record = {}
                        for i, column in enumerate(db.description):
                            record[column.name] = row[i]

                    return record
        except Exception:
            return {"message": "could not update relationship"}

    def delete_relationship(self, relationship_id) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE from relationships
                        WHERE id = %s
                        """,
                        [relationship_id],
                    )
                    return True
        except Exception:
            return False
