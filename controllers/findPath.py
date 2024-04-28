from fastapi import APIRouter
from pydantic import BaseModel
from services.navigation import *

router = APIRouter()

class Path(BaseModel):
    start: str
    goal: str

@router.post("")
async def find_path(req: Path):
    print("## find_path -> recieved")
    return await get_path(req)
