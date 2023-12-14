from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .models import Assistant
from common.database import get_db
from .db_models import AssistantDBModel
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
    assistant = db.query(AssistantDBModel).filter(AssistantDBModel.id == assistant_id).first()
    
    assistant_model = Assistant.from_orm(assistant)
    assistant_model.createTime = assistant.createTime
    assistant_model.updateTime = assistant.updateTime
    
    return assistant_model

@router.put("/{assistant_id}")
def update_assistant(assistant_id: UUID, assistant: Assistant, db: Session = Depends(get_db)):
    db_assistant = db.query(AssistantDBModel).filter(AssistantDBModel.id == assistant_id).first()
    db_assistant.update(**assistant.model_dump(exclude_unset=True))
    db.commit()
    return db_assistant

@router.delete("/{assistant_id}")
def delete_assistant(assistant_id: UUID, db: Session = Depends(get_db)):
    db.query(AssistantDBModel).filter(AssistantDBModel.id == assistant_id).delete()
    db.commit()
    return {"message": "Assistant deleted"}