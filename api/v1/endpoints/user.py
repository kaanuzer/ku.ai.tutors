from fastapi import APIRouter




router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"id": user_id, "name": "Example User"}