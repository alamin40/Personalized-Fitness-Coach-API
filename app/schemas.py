from pydantic import BaseModel
from typing import List, Optional

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: str
    goal: str  # 'lose weight', 'gain muscle', etc.

