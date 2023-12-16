# Importing The FastApi class
from fastapi import FastAPI

# Creating an app object
app = FastAPI()

# Defualt route 

# A minimal app to domenstrate the get request
@app.get("/",tags=['ROOT'])
async def root()->dict:
    return {"Hell": "World"}


# Get -> Read Todo
@app.get("/todo", tags = ['Todos'])
async def get_todos()->dict:
    return {"Data":todos}


# Post -> Create Todo
@app.post("/todo", tags=['Todos'])
async def add_todos(todo:dict)->dict:
    todos.append(todo)
    return{"data":"A todo is added!"}

# Put -> Update Todo
@app.put("/todo/{id}", tags=['Todos'])
async def update_todos(id: int, body: dict)->dict:
    for todo in todos:
        if int(todo['id'])==id:
            todo['Activity'] = body['Activity']
            return{
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }

# DELETE -> delete Todo
@app.delete("/todo/{id}", tags=['Todos'])
async def delete_todos(id : int)->dict:
    for todo in todos:
        if int(todo["id"])==id:
            todos.remove(todo)
            return{
                "data": f"Todo wiht id {id} has been delete"
            }
    return{
        "data": f"This Todo with {id} is not delete"
    }


# Todos List 
todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."

    },
    {
        "id": "2",
        "Activity": "Writing 3 page of my new books at 2.00 pm."
    }
]


