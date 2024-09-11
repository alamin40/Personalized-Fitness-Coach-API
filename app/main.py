from fastapi import FastAPI
from routers import users



app = FastAPI()


app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Personalized Fitness Coach API"}
