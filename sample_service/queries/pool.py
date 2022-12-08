import os
from psycopg_pool import ConnectionPool

db_url = os.environ.get("DATABASE_URL")
if db_url is not None:
    pool = ConnectionPool(conninfo=db_url)
else:
    pool = None
