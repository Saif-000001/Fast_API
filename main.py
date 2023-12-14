# from fastapi import FastAPI
# from typing import Optional

# app = FastAPI()

# @app.get("/")
# async def read_road():
#     return{"Hello":"World"}

# Path parameter with types
# @app.get("/iteams/{iteam_id}")
# async def read_iteam(iteam_id : int, q: Optional[str]=None):
#     return {"iteam_id": iteam_id, "q":q}

# Path parameter
# @app.get("/iteams/{item_id}")
# async def read_iteam(item_id):
#     return{"item_id":item_id}


from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name, "message": "Deep learning FTW"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "leCNN all the images"}
    
    return {"model_name": model_name, "message" : "Have some residuls"}
