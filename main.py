from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from handler import get_quiz

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicInput(BaseModel):
    topic: str

@app.post("/get_posts/")
def get_posts(input_data: TopicInput):
    try:
        topic = input_data.topic
        result = get_quiz(topic)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
