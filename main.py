from fastapi import FastAPI
from typing import Union
from views import main_view

app = FastAPI()


app.include_router(main_view.router,prefix='/api/v1')


