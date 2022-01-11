from chatModule import chat
from fastapi import Depends, FastAPI
from assessmentModule import assessment
app = FastAPI()

app.include_router(chat.router)
app.include_router(assessment.router)
