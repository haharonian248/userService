from fastapi import FastAPI
from controller.user_controller import router as user_router
from controller.user_answer_controller import router as user_answer_router
from repository.database import database

app = FastAPI()
app.include_router(user_router)
app.include_router(user_answer_router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()