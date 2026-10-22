from fastapi import FastAPI
from travel_agent_api.routes.chat_router import router as chat_router

app = FastAPI(
    title="Travel Agent API",
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def read_root():
    return {"message": "Benvenuto nella Travel Agent API di FastAPI e LangChain!"}