from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Physical AI & Humanoid Robotics Book Backend!"}

# Simple chat endpoint that echoes the message
@app.post("/chat")
def chat(chat_request: ChatRequest):
    user_message = chat_request.message
    bot_response = f"You asked: '{user_message}'. This is a basic response from the Physical AI & Humanoid Robotics assistant."
    return {"response": bot_response}

# RAG chat endpoint that echoes the message (placeholder for now)
@app.post("/chat_with_rag")
def chat_with_rag(chat_request: ChatRequest):
    user_message = chat_request.message
    bot_response = f"You asked: '{user_message}'. This is a RAG-enhanced response from the Physical AI & Humanoid Robotics assistant. (RAG functionality will be implemented when the full backend is operational)"
    return {"response": bot_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)