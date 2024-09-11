from sqlalchemy.orm import Session
from . import models, schemas

# Service to create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, goal=user.goal)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user