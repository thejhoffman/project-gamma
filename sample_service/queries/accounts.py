from pydantic import BaseModel
from queries.pool import pool


class DuplicateAccountError(ValueError):
    pass


class AccountIn(BaseModel):
    email: str
    password: str
    name: str


class AccountOut(BaseModel):
    id: int
    email: str
    name: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountQueries:
    def get(self, email: str) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, email, hashed_password, name
                        FROM accounts
                        WHERE email = %s
                        """,
                        [email]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return AccountOutWithPassword (
                        id = record[0],
                        email = record[1],
                        hashed_password = record[2],
                        name = record[3]
                    )
        except Exception as e:
            print(e)
            return {"message": "Could not get that user"}


    def create(self, info: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO accounts
                            (email, hashed_password, name)
                        VALUES
                            (%s, %s, %s)
                            RETURNING id;
                        """,
                        [
                            info.email,
                            hashed_password,
                            info.name
                        ]
                    )
                    id = result.fetchone()[0]
                    old_data = info.dict()
                    return AccountOutWithPassword(id=id, hashed_password=hashed_password, **old_data)
        except Exception:
            return {"message": "Create did not work"}
