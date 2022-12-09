from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import MessageSchema, FastMail, MessageType, ConnectionConfig
from starlette.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Dict
import os


router = APIRouter(tags=["Emails"])

class EmailSchema(BaseModel):
    email: str
    body: str

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
    TEMPLATE_FOLDER = './routers/templates'
)

@router.post("/api/email/welcome")
async def welcome_email(
    email: EmailSchema,
    body: Dict[str, Any]
    ) -> JSONResponse:

    message = MessageSchema(
        subject="Welcome to Largesseance",
        recipients=email,
        template_body=body,
        subtype=MessageType.html,)

    fm = FastMail(conf)

    await fm.send_message(message, template_name='welcome.html')

    return JSONResponse(status_code=200, content={"message": "email has been sent"})

@router.post("/api/email/notification")
async def notification_email(
    email: EmailSchema,
    body: Dict[str, Any]
    ) -> JSONResponse:

    message = MessageSchema(
        subject="You've successfully created a new event",
        recipients=email,
        template_body=body,
        subtype=MessageType.html,)

    fm = FastMail(conf)

    await fm.send_message(message, template_name='notification.html')

    return JSONResponse(status_code=200, content={"message": "email has been sent"})
