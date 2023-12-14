from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Assistant
from common.database import get_db
from .db_models import AssistantModel
from uuid import UUID

router = APIRouter(prefix="/assistant", tags=["assistant"])

@router.post("/")
def create_assistant(assistant: Assistant, db: Session = Depends(get_db)):
    db_assistant = assistant.to_orm()
    db.add(db_assistant)
    db.commit()
    db.refresh(db_assistant)
    return db_assistant

@router.get("/{assistant_id}")
def read_assistant(assistant_id: UUID, db: Session = Depends(get_db)):
    assistant = db.query(AssistantModel).filter(AssistantModel.id == assistant_id).first()
    return assistant

@router.put("/{assistant_id}")
def update_assistant(assistant_id: UUID, assistant: Assistant, db: Session = Depends(get_db)):
    db_assistant = db.query(AssistantModel).filter(AssistantModel.id == assistant_id).first()
    for key, value in assistant.model_dump(exclude_unset=True).items():
        setattr(db_assistant, key, value)
    db.commit()
    return db_assistant

@router.delete("/{assistant_id}")
def delete_assistant(assistant_id: UUID, db: Session = Depends(get_db)):
    db.query(AssistantModel).filter(AssistantModel.id == assistant_id).delete()
    db.commit()
    return {"message": "Assistant deleted"}