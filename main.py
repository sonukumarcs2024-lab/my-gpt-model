 from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

HF_TOKEN = os.environ.get("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")

API_URL = "https://api-inference.huggingface.co/models/google/gemma-2b"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "GPT API running"}

@app.post("/chat")
def chat(req: ChatRequest):

    payload = {
        "inputs": req.prompt,
        "parameters": {"max_new_tokens": 200}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    return response.json()
