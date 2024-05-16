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



@router.post("/add/", response_model=schemas.Persona)
def create_user(persona: schemas.Persona, db: Session = Depends(get_db)):
    persona_db = crud.get_persona(db,persona.dni)
    if persona_db:
        raise HTTPException(status_code=400, detail="Person already registered")
    
    return crud.created_persona(db=db, persona=persona)


@router.get('/all',response_model=list[schemas.Persona])
async def personas(skip:int=0,limit:int=100, db:Session=Depends(get_db)):
    personas = crud.get_personas(db=db,skip=skip,limit=limit)
    return personas



@router.get('/get_personas')
async def get_personas():
    pass
    