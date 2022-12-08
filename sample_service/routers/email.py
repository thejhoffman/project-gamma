from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import MessageSchema, FastMail, MessageType, ConnectionConfig
from starlette.responses import JSONResponse
from pydantic import BaseModel
import os


router = APIRouter(tags=["Emails"])

class EmailSchema(BaseModel):
    email: str

conf = ConnectionConfig(
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD"),
    MAIL_FROM = os.environ.get("MAIL_FROM"),
    MAIL_PORT = int(os.environ.get("MAIL_PORT")),
    MAIL_SERVER = os.environ.get("MAIL_SERVER"),
    MAIL_FROM_NAME = os.environ.get("MAIL_FROM_NAME"),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    TEMPLATE_FOLDER = './templates'
)


@router.post("/welcome_email")
async def welcome_email(
    email: EmailSchema
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Welcome to Largesseance",
        recipients=email,
        body="Thank you for signing up!",
        subtype=MessageType.html,)

    fm = FastMail(conf)

    await fm.send_message(message)

    return JSONResponse(status_code=200, content={"message": "email has been sent"})