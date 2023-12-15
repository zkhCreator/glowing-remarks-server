import logging
from fastapi import APIRouter, FastAPI
from common.database import on_startup
from assistant.route import router as assistant_router
from auth.route import router as auth_router
import uvicorn

app = FastAPI()

# 启用 SQLAlchemy 的日志记录
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


app.add_event_handler("startup", on_startup)

app.include_router(assistant_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )

