from fastapi import FastAPI
from typing import Union
from views import main_view,persona_view
# from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1",
#     "http://127.0.0.1:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


app.include_router(main_view.router,prefix='/api/v1')
app.include_router(persona_view.router,prefix='/api/v1/Persona')

