from fastapi import FastAPI
from pydantic import BaseModel
from controllers.calculateLocation import router as calculateLocation_router

app = FastAPI()

app.include_router(calculateLocation_router, prefix="/mylocation", tags=["my-location"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


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