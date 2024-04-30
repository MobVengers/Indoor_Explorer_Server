from utils.accessPoint import *
from utils.calibrationPoints import *
from fastapi.responses import JSONResponse
from models.adminKey import *
import hashlib

async def create_calibration_fingerprint(req):
    
    admin_key = req.adminKey
    
    hashed_key_obj = AdminKey.objects().first()
    if not hashed_key_obj:
        err = "There is no admin key in the DB"
        return JSONResponse(content={"message": str(err)}, status_code=500)

        
    try:
        if hashlib.sha256(admin_key.encode()).hexdigest() == hashed_key_obj.hashkey:
            project_id = req.projectId
            received_signals = req.received_signals
            await create_non_existing_access_points(received_signals, project_id)
            await create_calibration_point(req)
            return JSONResponse(content={"message": "FingerPrint Added"}, status_code=200)
        else:
            err = "Wrong admin key"
            return JSONResponse(content={"message": str(err)}, status_code=500)
    except Exception as err:
        return JSONResponse(content={"message": str(err)}, status_code=500)
    

async def create_non_existing_access_points(access_points, project_id):
    access_points_in_database = await get_access_points_by_id(project_id)
    access_points_in_database_bssids = [ap.bssid for ap in access_points_in_database]
    new_access_points = [ap for ap in access_points if ap.bssid not in access_points_in_database_bssids]
    if len(new_access_points) > 0:
        await add_multiple_access_points(new_access_points, project_id)