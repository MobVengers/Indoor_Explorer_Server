from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.createCalibrationFingerprint import *
import hashlib

router = APIRouter()

class ReceivedSignal(BaseModel):
    bssid: str
    ssid: str
    rssi: float
    

class NewFingerPrint(BaseModel):
    projectId: str
    adminKey: str
    pos_x: float
    pos_y: float
    received_signals: List[ReceivedSignal]

@router.post("/create")
async def create_fingerprint(req: NewFingerPrint):
    print("## create_fingerprint -> recieved")
    print("## req:", req)
    return await create_calibration_fingerprint(req)




class AdminKey(BaseModel):
    key: str

@router.post("/hashkey")
def get_hash_key(req: AdminKey):
    print("## get_hash_key -> recieved")
    return JSONResponse(content={"hash_key": str(hashlib.sha256(req.key.encode()).hexdigest())}, status_code=200)
       
