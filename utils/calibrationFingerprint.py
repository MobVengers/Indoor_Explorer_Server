import uuid
from models.calibrationFingerprint import CalibrationFingerprint

async def create_fingerprint_from_request(req_body):
    received_signals = req_body.get("received_signals", [])
    calibration_fingerprint_to_create = CalibrationFingerprint(
        id=str(uuid.uuid4()),
        projectId=req_body["projectId"],
        calibrationPointId=req_body["calibrationpointID"],
        radioMap={},
    )
    for signal in received_signals:
        calibration_fingerprint_to_create.radioMap[signal["bssid"]] = signal["rss"]
    await calibration_fingerprint_to_create.save()