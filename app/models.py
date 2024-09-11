from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# SQLAlchemy model for users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    goal = Column(String)

    workout_logs = relationship("WorkoutLog", back_populates="user")

# SQLAlchemy model for workout logs
class WorkoutLog(Base):
    __tablename__ = "workout_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    workout = Column(String)
    reps = Column(Integer)

    user = relationship("User", back_populates="workout_logs")
