from sqlalchemy.orm import Session

from . import models, schemas


### Personas Controllers


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

def update_persona(db: Session, id: int, persona: schemas.Persona):
    persona_db = db.query(models.Persona).filter(models.Persona.idpersona == id).first()
    if persona_db:
        for attr, value in persona.dict(exclude_unset=True).items():
            if hasattr(persona_db, attr):
                setattr(persona_db, attr, value)
        db.commit()
        db.refresh(persona_db)
        return persona_db
  
def delete_persona(db: Session, id: int):

    persona_db = db.query(models.Persona).filter(models.Persona.idpersona == id).first()
    if persona_db:
   
        db.delete(persona_db)
        db.commit()
        return persona_db
    else:
   
        return None  



###tasks Controllers


def create_task(db:Session,tasks:schemas.CreateTask,persona_id:int):
    
    db_tasks = models.tasks(**tasks.dict(),persona_id=persona_id )
    db.add(db_tasks)
    db.commit()
    db.refresh(db_tasks)
    return db_tasks
