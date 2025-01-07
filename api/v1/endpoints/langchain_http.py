from fastapi import  APIRouter,HTTPException,Query
from services.langchain_service import generate_response

router = APIRouter(prefix="/langchain", tags=["langchain"])


@router.post("/generate")
async def generate_text(prompt:str = Query(..., description="Text to generate")):
    try:
        response = await generate_response(prompt)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))