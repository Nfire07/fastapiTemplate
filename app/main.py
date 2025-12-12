from fastapi import FastAPI
from .modules import users

app = FastAPI()

app.include_router(users.router)
