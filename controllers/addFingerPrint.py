from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict
from services.createCalibrationFingerprint import *

router = APIRouter()

class NewFingerPrint(BaseModel):
    projectId: str
    received_signals: Dict[str, int]

@router.get("/create")
async def create_fingerprint(req: NewFingerPrint):
    print("## recieved")
    return await create_calibration_fingerprint(req)