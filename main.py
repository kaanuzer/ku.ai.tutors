from fastapi import FastAPI
from api.v1.endpoints.user import router as user_router
from api.v1.endpoints.learning import router as learning_router
from api.v1.endpoints.langchain_ws import router as langchain_ws_router
from api.v1.endpoints.langchain_http import router as langchain_http_router

app = FastAPI(title="Education Assistant API", version="1.0.0")



@app.get("/")
async def root():
    return {"message": "Welcome to Education Assistant API"}


app.include_router(user_router, prefix="/api")
app.include_router(learning_router, prefix="/api")

app.include_router(langchain_ws_router, prefix="/api")

app.include_router(langchain_http_router, prefix="/api")