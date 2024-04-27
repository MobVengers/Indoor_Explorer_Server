from fastapi import APIRouter
from pydantic import BaseModel
from services.navigation import *

router = APIRouter()

class Path(BaseModel):
    start: str
    goal: str

@router.get("/")
async def find_path(req: Path):
    return await get_path(req)
