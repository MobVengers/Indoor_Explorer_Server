from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from controllers.calculateLocation import router as calculateLocation_router
from controllers.addFingerPrint import router as addFingerPrint_router
from controllers.healthCheck import router as healthCheck_router
from controllers.findPath import router as findPath_router
from db_connect import *
from dotenv import load_dotenv

load_dotenv()

initialize_db()

app = FastAPI()

app.include_router(calculateLocation_router, prefix="/mylocation", tags=["my-location"])
app.include_router(addFingerPrint_router, prefix="/fingerprint", tags=["finger-print"])
app.include_router(healthCheck_router, prefix="/health", tags=["health-check"])
app.include_router(findPath_router, prefix="/path", tags=["path"])

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)