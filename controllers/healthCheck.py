from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
async def read_root():
    return {"status": "active"}



