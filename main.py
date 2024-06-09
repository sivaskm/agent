from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from handler import get_quiz, get_evaluation

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

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


class QuizItem(BaseModel):
    question: str
    correct_answer: str
    difficulty_level: str  # Note: There seems to be a typo in the original data, should be 'difficulty_level'
    topic: str
    all_options: List[str]
    selected_answer: str


@app.post("/get_posts/")
def get_posts(input_data: TopicInput):
    try:
        topic = input_data.topic
        result = get_quiz(topic)
        print(result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/submit-quiz/")
async def submit_quiz(quiz: List[QuizItem]):
    try:
        evaluation = get_evaluation(quiz)
        print(evaluation)
        return evaluation
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
