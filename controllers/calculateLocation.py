from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RequestBody1(BaseModel):
    name: str
    age: int

@router.get("/")
async def myloc(req: RequestBody1):
    
    print(req.name)

    # calculateLocation(RequestBody)

    return {"location": f"x:{10}, y={20}"}