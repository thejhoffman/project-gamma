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
    people,
    products,
    email
)
import os
import asyncio
import uvicorn
from routers.scheduler import app as app_rocketry

class Server(uvicorn.Server):
    """Customized uvicorn.Server

    Uvicorn server overrides signals and we need to include
    Rocketry to the signals."""
    def handle_exit(self, sig: int, frame) -> None:
        app_rocketry.session.shut_down()
        return super().handle_exit(sig, frame)


async def main():
    "Run scheduler and the API"
    server = Server(config=uvicorn.Config(email, workers=1, loop="asyncio"))

    api = asyncio.create_task(server.serve())
    sched = asyncio.create_task(app_rocketry.serve())

    await asyncio.wait([sched, api])

if __name__ == "__main__":
    asyncio.run(main())

app = FastAPI()
app.include_router(email.router)
app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(relationships.router)
app.include_router(occasions.router)
app.include_router(events.router)
app.include_router(age_range.router)
app.include_router(interests.router)
app.include_router(gender.router)
app.include_router(people.router)
app.include_router(products.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
