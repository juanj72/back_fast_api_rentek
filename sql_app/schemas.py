from pydantic import BaseModel
from datetime import datetime, date



    
class TaskBase(BaseModel):
    description_task: str
    created_date: datetime
    due_date: date

class CreateTask(TaskBase):
    pass

class GetTask(TaskBase):
    id: int


class Persona(BaseModel):
    
    first_name: str
    last_name: str
    dni: int
    taskss: list[GetTask]=[]
    class Config:
        orm_mode = True


class get_Persona(Persona):
    idpersona: int