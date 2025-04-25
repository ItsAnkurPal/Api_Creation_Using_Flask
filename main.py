from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
from typing import Optional


load_dotenv()
app = FastAPI()


class AgentRequest(BaseModel):
    provider: str
    name: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the Agent Creation API! Type /docs in url for Swagger UI."}

@app.post("/create-agent")
def create_agent(request: AgentRequest):
    if request.provider == "vapi":
        return call_vapi_api(request.name)
    elif request.provider == "retell":
        return call_retell_api(request.name)
    else:
        raise HTTPException(status_code=400, detail="Invalid provider")

def call_vapi_api(name: str):
    url = "https://api.vapi.ai/assistant"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "name": "Ankur VAPI Agent",  # hardcoded internally
        "model": "gpt-3.5-turbo"  # hardcoded internally
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

def call_retell_api(name: str):
    url = "https://api.retellai.com/create-agent"
    headers = {
        "Authorization": f"Bearer {os.getenv('RETELL_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "response_engine": {
            "type": "retell-llm",
            "llm_id": "llm_9c7545e93e1d6a7916c34d5b21ff"  # hardcoded internally, Because this field were required In retell but not in vapi
        },
        "agent_name": "Ankur Retell Agent",
        "voice_id": "11labs-Amritanshu"  # hardcoded internally, Because this field were required In retell but not in vapi
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()
