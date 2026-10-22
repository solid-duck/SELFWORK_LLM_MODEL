from fastapi import APIRouter
from pydantic import BaseModel
from travel_agent_api.services.agent_service import Agent

router = APIRouter()

class ChatCompletionRequest(BaseModel):
    messages: list

    model_config = {
        "json_schema_extra": {
            "example": {
                "messages": [
                    {
                        "role": "user",
                        "content": "Vorrei organizzare un viaggio a Roma"
                    }
                ]
            }
        }
    }

@router.post("/travel-agent")
def chat_completion(request: ChatCompletionRequest):
    agent_instance = Agent()
    response = agent_instance.run(messages=request.messages)
    
    print(" " * 80)
    print("chat_completion")
    print("*" * 80)
    
    return response