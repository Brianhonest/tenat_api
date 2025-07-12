from fastapi import FastAPI,Form
from typing import Annotated
from . import schemas
app = FastAPI()


@app.get("/")
def root():
    return{"message":"Welcome to my tenats"}

@app.post("/login")
async def login(data:Annotated[schemas.UserIn,Form()]):
    return data

@app.get("/tenats")
def get_tenats():
