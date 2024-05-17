from fastapi import APIRouter, HTTPException,Depends
# from sql_app.schemas import *
from sqlalchemy.orm import Session


from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post('/{user_id}/create',response_model=schemas.CreateTask)
async def create_task(task:schemas.CreateTask,user_id,db:Session = Depends(get_db)):
    tasks_db = crud.create_task(db=db,tasks=task,persona_id=user_id)
    if tasks_db:
        return tasks_db
    else:
         raise HTTPException(status_code=400, detail="i don't know what's the error")