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



