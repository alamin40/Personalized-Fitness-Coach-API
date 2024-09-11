from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class User(BaseModel):
    name: str
    email: str
    goal: str  # E.g., 'lose weight', 'gain muscle'

users_db = []

@router.post("/users/")
async def create_user(user: User):
    users_db.append(user)
    return {"message": "User registered successfully", "user": user}

