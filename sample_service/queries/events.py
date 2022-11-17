from pydantic import BaseModel


class EventIn(BaseModel):
    name: str
    date: str
    person_id: int
    occasion_id: int
    account_id: int


#  CREATE TABLE events (
#             id SERIAL PRIMARY KEY NOT NULL,
#             name VARCHAR(100) NOT NULL,
#             date DATE NOT NULL,
#             person_id INTEGER NOT NULL REFERENCES person("id") ON DELETE RESTRICT,
#             occasion_id INTEGER REFERENCES occasion("id") ON DELETE RESTRICT,
#             account_id SERIAL NOT NULL REFERENCES accounts("id") ON DELETE CASCADE
#         );
