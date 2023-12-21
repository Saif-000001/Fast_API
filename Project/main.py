from typing import List
from fastapi import FastAPI
from models import User, Gender, Role
app = FastAPI()

db:List[User] = [
    User(
        first_name="Jamala",
        last_name="Ahmed",
        gender=Gender.female,
        roles = [Role.student]
    )
]

@app.get("/")
async def root():
    return {"massege":"Hello World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db