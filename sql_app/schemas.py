from pydantic import BaseModel,Field
from datetime import datetime, date



    
class TaskBase(BaseModel):
    description_task: str
    created_date: datetime = Field(default_factory=datetime.now)
    due_date: date

class CreateTask(TaskBase):
    pass

class GetTask(TaskBase):
    id: int


class Persona(BaseModel):
    
    first_name: str
    last_name: str
    dni: int
    taskss: list[TaskBase]=[]
    class Config:
        from_attributes = True


class get_Persona(Persona):
    idpersona: int
    taskss: list[TaskBase]=[]