from twilio.rest import Client
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.get_connection import GetConnection
from psycopg2.extras import RealDictCursor
import psycopg2
from utils.send_email import EmailSender

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(6))
    return otp


class SendOTP(APIView):
    def send_otp(to_email, first_name):
        otp_code = generate_otp()
        
        connection = GetConnection.get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        emailer = EmailSender()
        sent_email = emailer.send_email(
            to_email=to_email,
            subject="OTP to verify your email",
            body='Hey! \nPlease enter the following OTP to verify your email.\n'+otp_code
        ).__dict__
        print('sent_email otp', otp_code)

        email_response = sent_email.get('data')
        if(email_response.get('status_code') == 200):
            cursor.execute("""UPDATE users SET otp = %s WHERE email=%s""", (
                otp_code,
                to_email,
            ))
            connection.commit()
        

            return Response(
                {
                    'status_code': status.HTTP_200_OK,
                    'message': 'OTP sent successfully'
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'OTP sent fail'
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def expire_otp(to_phone_number):
        connection = GetConnection.get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        cursor.execute("""UPDATE users SET otp = %s WHERE phone_number=%s""", (
            0,
            to_phone_number,
        ))
        connection.commit()
        
        return Response(
            {
                'status_code': status.HTTP_200_OK,
                'message': 'OTP expired'
            },
            status=status.HTTP_200_OK
        )
