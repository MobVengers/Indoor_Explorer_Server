from fastapi import APIRouter
from pydantic import BaseModel
from ..services.calculatePosition import calculate_position

router = APIRouter()

class RequestBody(BaseModel):
    projectId: str
    received_signals: int

@router.get("/")
async def myloc(req: RequestBody):
    
    print(req.name)

    # return calculate_position(req)

    return {"location": f"x:{10}, y={20}"}