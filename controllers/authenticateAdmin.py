from fastapi import APIRouter
from pydantic import BaseModel
import hashlib
from fastapi.responses import JSONResponse
from services.authenticateAdmin import *

router = APIRouter()


class AdminKey(BaseModel):
    adminKey: str

@router.post("/hashkey")
def get_hash_key(req: AdminKey):
    print("## get_hash_key -> recieved")
    return JSONResponse(content={"hashKey": str(hashlib.sha256(req.adminKey.encode()).hexdigest())}, status_code=200)
       
@router.post("")
def auth_admin(req: AdminKey):
    print("## get_hash_key -> recieved")
    return authenticate_admin(req)
