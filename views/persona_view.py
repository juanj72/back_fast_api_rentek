from fastapi import APIRouter, HTTPException,Depends
# from sql_app.schemas import *
from sqlalchemy.orm import Session
from datetime import datetime

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



@router.post("/add/", response_model=schemas.Persona)
def create_user(persona: schemas.Persona, db: Session = Depends(get_db)):
    persona_db = crud.get_persona(db,persona.dni)
    if persona_db:
        raise HTTPException(status_code=400, detail="Person already registered")
    else:
    
        return crud.created_persona(db=db, persona=persona)


@router.get('/all',response_model=list[schemas.get_Persona])
async def personas(skip:int=0,limit:int=100, db:Session=Depends(get_db)):
    personas = crud.get_personas(db=db,skip=skip,limit=limit)
    for persona in personas:
        for task in persona.taskss:
            if task.created_date is None:
                task.created_date = datetime.utcnow()  
    return personas


@router.patch('/update/{id}',response_model=schemas.Persona)
async def update_persona(persona:schemas.Persona,id,db:Session=Depends(get_db)):
    persona_db = crud.update_persona(db, id, persona)
    if persona_db:
        return persona_db
    else:
        raise HTTPException(status_code=400, detail="Person not registered")


    
@router.delete('/delete/{id}',response_model=schemas.get_Persona)
async def delete_persona(id,db:Session=Depends(get_db)):
    person_db = crud.delete_persona(db,id)
    if not person_db:
        raise HTTPException(status_code=400, detail="Person not registered")
    return person_db

