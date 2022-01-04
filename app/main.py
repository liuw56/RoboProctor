from chatModule import chat
from fastapi import Depends, FastAPI

app = FastAPI()

app.include_router(chat.router)
