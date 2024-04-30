import hashlib
from fastapi.responses import JSONResponse
from utils.adminKey import *

def authenticate_admin(req):
    admin_key = req.adminKey
    hashed_key_obj_from_db = get_admin_keys()
    if hashlib.sha256(admin_key.encode()).hexdigest() == hashed_key_obj_from_db.hashkey:
        return JSONResponse(content={"message": "true"}, status_code=500)

    else:
        return JSONResponse(content={"message": "false"}, status_code=500)
    