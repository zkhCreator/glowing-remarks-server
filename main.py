from typing import Union
from fastapi import FastAPI
from common.database import startup, shutdown
from assistant.route import router as assistant_router

app = FastAPI()

app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

app.include_router(assistant_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
