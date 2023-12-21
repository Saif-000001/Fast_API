from myModul import User

from fastapi import FastAPI
app = FastAPI()

db:User()

@app.get("/")
async def root():
   
    return{"YES"}