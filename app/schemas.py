from pydantic import BaseModel
from typing import List, Optional

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    goal: str  # 'lose weight', 'gain muscle', etc.

# Schema for retrieving a user (can include other fields like ID)
class User(BaseModel):
    id: int
    name: str
    email: str
    goal: str

    class Config:
        orm_mode = True

# Schema for logging a workout
class WorkoutLogCreate(BaseModel):
    user_id: int
    workout: str
    reps: int

# Schema for returning a logged workout
class WorkoutLog(BaseModel):
    id: int
    user_id: int
    workout: str
    reps: int

    class Config:
        orm_mode = True
