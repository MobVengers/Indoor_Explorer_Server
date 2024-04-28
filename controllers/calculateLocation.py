from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.calculatePosition import *

router = APIRouter()

class ReceivedSignal(BaseModel):
    bssid: str
    ssid: str
    rssi: float

class CurrentFingerPrint(BaseModel):
    projectId: str
    received_signals: List[ReceivedSignal]

@router.post("/")
async def myloc(req: CurrentFingerPrint):
    print("## mylocation -> recieved")
    print("## req:", req)
    return await calculate_position(req)

