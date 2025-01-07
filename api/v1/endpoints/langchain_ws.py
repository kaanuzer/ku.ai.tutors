from fastapi import WebSocket,APIRouter
from realtime.websocket_manager import  WebSocketManager
from services.langchain_service import generate_response



router = APIRouter()
ws_manager = WebSocketManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            response = await generate_response(data)

            await ws_manager.send_message(response)
    finally:
        await ws_manager.disconnect(websocket)
