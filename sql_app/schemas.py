from pydantic import BaseModel



class Persona(BaseModel):
    
    first_name: str
    last_name: str
    dni: int


class get_Persona(BaseModel):
    idpersona: int
    first_name: str
    last_name: str
    dni: int

