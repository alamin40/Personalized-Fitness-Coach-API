from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class User(BaseModel):
    name: str
    email: str
    goal: str  # E.g., 'lose weight', 'gain muscle'

users_db = []


