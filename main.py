import logging
import os

from fastapi import FastAPI

app = FastAPI()
logger = logging.Logger("my-logger")


@app.get("/")
async def root():
    conn_string = os.environ.get("DB_CONNECTION_STRING", "FALSE")
    logger.info(conn_string)
    return {"message": conn_string}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
