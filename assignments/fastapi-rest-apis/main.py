from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Activity(BaseModel):
    name: str
    description: str
    schedule: str
    max_participants: int
    participants: List[str] = []

activities: Dict[str, Activity] = {}

@app.get("/")
def read_root():
    return {"message": "Welcome to Mergington High School API!"}

# TODO: Implement Task 2 CRUD endpoints here
