from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from authenticator import authenticator
from routers import (
    accounts,
    events,
    age_range,
    interests,
    relationships,
    occasions,
    gender,
)
import os

app = FastAPI()
app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(relationships.router)
app.include_router(occasions.router)
app.include_router(events.router)
app.include_router(age_range.router)
app.include_router(interests.router)
app.include_router(gender.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
