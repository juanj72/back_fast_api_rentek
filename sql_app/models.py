from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Persona(Base):
    __tablename__ = "persona"

    idpersona = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dni = Column(Integer,unique=True)
    taskss = relationship('tasks',back_populates='persona')


class tasks(Base):
    __tablename__ = 'tasks'
    id =Column(Integer,primary_key=True)
    description_task = Column(String)
    created_date = Column(DateTime, default=datetime.utcnow)
    due_date = Column(Date)
    persona_id = Column(Integer,ForeignKey('persona.idpersona'))

    persona = relationship('Persona',back_populates='taskss')

    


