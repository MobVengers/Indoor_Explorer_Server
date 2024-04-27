from fastapi import FastAPI
from pydantic import BaseModel
from controllers.calculateLocation import router as calculateLocation_router
from controllers.addFingerPrint import router as addFingerPrint_router
from controllers.healthCheck import router as healthCheck_router
from db_connect import *

initialize_db()

app = FastAPI()

app.include_router(calculateLocation_router, prefix="/mylocation", tags=["my-location"])
app.include_router(addFingerPrint_router, prefix="/fingerprint", tags=["finger-print"])
app.include_router(healthCheck_router, prefix="/health", tags=["health-check"])





# sample codes 

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


class RequestBody(BaseModel):
    name: str
    age: int

@app.get("/submit")
async def submit_data(req: RequestBody):
    # Access the request body using the Pydantic model
    name = req.name
    age = req.age

    return {"message": f"Received data: Name={name}, Age={age}"}