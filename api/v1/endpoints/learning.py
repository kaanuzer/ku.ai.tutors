
from fastapi import APIRouter


router = APIRouter(prefix="/learning", tags=["Learning"])


@router.get("/lesson")
async def getLesson():
    return { "Lessons": "Example Lessons"}