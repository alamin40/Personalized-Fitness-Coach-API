from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL (you can change this to any database like PostgreSQL, MySQL, etc.)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the engine that will manage the connection to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a sessionmaker to generate new sessions to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for ORM models
Base = declarative_base()
