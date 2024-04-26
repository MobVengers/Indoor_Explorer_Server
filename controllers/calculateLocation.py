from fastapi import APIRouter
from pydantic import BaseModel
from services.calculatePosition import *

router = APIRouter()

class RequestBody(BaseModel):
    projectId: str
    received_signals: int

@router.get("/")
async def myloc(req: RequestBody):
    
    print(req.name)

    return calculate_position(req)

    # return {"location": f"x:{10}, y={20}"}

# NOTE: Refer calibrate.py and createCalibrationFingerprint.py for 
# a better implementation of the API endpoints