from typing import List
from uuid import uuid4
from fastapi import FastAPI
from . import models

app = FastAPI()

db: List[models.User]=[
    models.User(
        id=uuid4(),
        first_name = "Jamila",
        last_name = "Ahmed",
        gender = models.Gender.female,
        roles = [models.Role.student]
    ),
    models.User(
        id = uuid4(),
        first_name = "Alex",
        last_name = "Jones",
        gender = models.Gender.male,
        roles = [models.Role.admin, models.Role.user]
    )

]

@app.get("/")
async def root():
    return {"Massege":"Hello World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;
