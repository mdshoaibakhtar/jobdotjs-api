import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from rest_framework.response import Response
from rest_framework import status
import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

class EmailSender:
    def __init__(self):
        if os.environ.get("VERCEL_ENV") is None:
            env_path = Path(__file__).resolve().parent.parent / '.env'
            load_dotenv(dotenv_path=env_path)

        self.sender_email = os.getenv("SENDER_EMAIL")
        self.sender_password = os.getenv("SENDER_PASSWORD")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email(self, to_email: str, subject: str, body: str):
        try:
            msg = MIMEMultipart()
            msg["From"] = self.sender_email
            msg["To"] = to_email
            msg["Subject"] = subject

            msg.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            print("✅ Email sent successfully.")
            return Response(
            {
                'status_code': status.HTTP_200_OK,
                'message': 'Email sent successfully.'
            },
            status=status.HTTP_200_OK
        )
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            return Response(
            {
                'status_code': status.HTTP_400_OK,
                'message': 'Failed to send email'
            },
            status=status.HTTP_400_OK
            )