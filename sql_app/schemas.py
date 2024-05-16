from pydantic import BaseModel



class Persona(BaseModel):
    idpersona: int
    first_name: str
    last_name: str
    dni: int
