from fastapi import FastAPI

app = FastAPI()

# A minimal app to demonstrate the get request
@app.get("/")
async def root():
    return {"hell":"world"}


# get -> Read or output
@app.get("/worker", tags=['Worker'] )
async def get_workers():
    # return Workers
    return {
        "data":Workers
    }



# post -> crete or new data add in list
@app.post("/worker", tags=['Workers'])
async def add_worker(work : dict):
    Workers.append(work)
    return{"data": "Warker is added!"}


# put -> update or modify 
@app.put("/worker/{id}", tags=['Workers'])
async def update_worker(id:int, name:dict):
    for worker in Workers:
        if (int(worker["id"]))==id:
            worker["name"]=name["name"]
            return{"data":f"Worker with id {id} has been updated!"}
    return{"data": f"Worker with id {id} is not update!"}


# delete -> remove 
@app.delete("/worker/{id}", tags=['Workers'])
async def remove_worker(id:int):
    for worker in Workers:
        if (int(worker["id"]))==id:
           Workers.remove(worker)
           return{"data": f"Worker with id {id} has been deleted!"}
    return{"data": f"Worker with id {id} is not dalete!"}


# List of worker
Workers=[
    {
        "id":"1",
        "name":"Mr. YoYo"
    },
    {
        "id":"2",
        "name":"Mr. ZoZu"
    },
    {
        "id":"3",
        "name":"Mr. Mone"
    }
]