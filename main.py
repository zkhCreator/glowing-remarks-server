from typing import Any, Dict, Union
from fastapi import FastAPI
from common.database import startup, shutdown
from assistant.route import router as assistant_router
import uvicorn
import auth0
from pydantic import BaseModel
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

app.include_router(assistant_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.post("/users")
# def create_user(user: Dict[Any, Any]):
#     logging.debug("-------")
#     logging.debug(user)
#     return {"hello": "world"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )

