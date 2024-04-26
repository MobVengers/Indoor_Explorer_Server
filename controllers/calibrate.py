from fastapi import APIRouter, Request
from services.createCalibrationFingerprint import *

router = APIRouter()

@router.post("/fingerprint/create")
async def create_fingerprint(req: Request):
    return await create_calibration_fingerprint(req)