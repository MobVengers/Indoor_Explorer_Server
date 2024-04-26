from fastapi import APIRouter
from pydantic import BaseModel
from ..services import calculatePosition

router = APIRouter()

class RequestBody(BaseModel):
    projectId: str
    received_signals: int

@router.get("/")
async def myloc(req: RequestBody):
    
    print(req.name)

    # return calculatePosition.calculate_position(req)

    return {"location": f"x:{10}, y={20}"}