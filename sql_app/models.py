from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Persona(Base):
    __tablename__ = "persona"

    idpersona = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    dni = Column(Integer,unique=True)

    


