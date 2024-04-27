from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.createCalibrationFingerprint import *

router = APIRouter()

class ReceivedSignal(BaseModel):
    bssid: str
    ssid: str
    rssi: float
    

class NewFingerPrint(BaseModel):
    projectId: str
    pos_x: float
    pos_y: float
    received_signals: List[ReceivedSignal]

@router.get("/create")
async def create_fingerprint(req: NewFingerPrint):
    print("## recieved")
    return await create_calibration_fingerprint(req)