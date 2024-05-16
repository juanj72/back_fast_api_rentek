from sqlalchemy.orm import Session

from . import models, schemas


def created_persona(db: Session, persona: schemas.Persona):
    
    db_user = models.Persona(first_name=persona.first_name, last_name = persona.last_name, dni=persona.dni)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_persona(db:Session,dni:int):
    return db.query(models.Persona).filter(models.Persona.dni==dni).first()

def get_personas(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Persona).offset(skip).limit(limit).all()