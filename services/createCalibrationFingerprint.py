from utils.accessPoint import get_access_points_by_id, add_multiple_access_points
from utils.calibrationFingerprint import create_fingerprint_from_request
from utils.calibrationPoints import create_calibration_point
from fastapi.responses import JSONResponse

async def create_calibration_fingerprint(req):
    try:
        req_body = await req.json()
        project_id = req_body.get("projectId")
        received_signals = req_body.get("received_signals", [])
        await create_non_existing_access_points(received_signals, project_id)
        await create_fingerprint_from_request(req_body)
        await create_calibration_point(req_body)
        return JSONResponse(content={"message": "DONE"}, status_code=200)
    except Exception as err:
        return JSONResponse(content={"message": str(err)}, status_code=500)
    
async def update_radio_map(project_id):
    # TODO: IMPLEMENT THIS AND THE REST
    pass

async def create_non_existing_access_points(access_points, project_id):
    access_points_in_database = await get_access_points_by_id(project_id)
    access_points_in_database_bssids = [ap["bssid"] for ap in access_points_in_database]
    new_access_points = [ap for ap in access_points if ap["bssid"] not in access_points_in_database_bssids]
    await add_multiple_access_points(new_access_points, project_id)