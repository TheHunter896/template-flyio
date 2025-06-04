import logging
import os

from fastapi import FastAPI
from psycopg import connect

app = FastAPI()
logger = logging.Logger("my-logger")


@app.get("/")
async def root():
    conn_string = os.environ.get("DB_CONNECTION_STRING", "FALSE")
    logger.info(conn_string)
    return {"message": conn_string}


@app.get("/create-table/{name}")
async def create_table(name: str):
    conn = connect(conninfo=os.environ.get("DB_CONNECTION_STRING"))
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {name} ( name varchar(250) );")
    conn.commit()

    cursor.execute(f"SELECT * FROM {name}")

    return {"message": cursor.fetchall()}


@app.get("/get-items/{name}")
async def get_items(name: str):
    conn = connect(conninfo=os.environ.get("DB_CONNECTION_STRING"))
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {name}")

    return {"message": cursor.fetchall()}
