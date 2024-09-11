from sqlalchemy.orm import Session
from . import models, schemas

# Service to create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, goal=user.goal)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
  
# Service to get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()   
  
  # Service to log a workout
def log_workout(db: Session, workout_log: schemas.WorkoutLogCreate):
    db_log = models.WorkoutLog(user_id=workout_log.user_id, workout=workout_log.workout, reps=workout_log.reps)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log