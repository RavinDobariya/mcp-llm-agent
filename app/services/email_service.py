import os
import aiosmtplib       #SMTP used to send email to Gmail server
from email.message import EmailMessage


async def send_email_service(to: str, subject: str, body: str) -> str:
    message = EmailMessage()
    message["From"] = os.getenv("EMAIL_USER")
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)

    try:
        await aiosmtplib.send(
            message,
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,                     #encrypt connection to Gmail server
            username=os.getenv("EMAIL_USER"),
            password=os.getenv("EMAIL_PASS"),
        )
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {str(e)}"