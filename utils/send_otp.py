from twilio.rest import Client
import random
import string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.get_connection import GetConnection
from psycopg2.extras import RealDictCursor
import psycopg2

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for _ in range(6))
    return otp


class SendOTP(APIView):
    def send_otp(to_phone_number):
        otp_code = generate_otp()
        
        connection = GetConnection.get_connection()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        
        print('otp_code', otp_code)
        
        # client = Client(account_sid, auth_token)
        
        # message = client.messages.create(
        #     body=f"Your OTP code is {otp_code}",
        #     from_=twilio_phone_number,
        #     to=to_phone_number
        # )
        
        cursor.execute("""UPDATE users SET otp = %s WHERE phone_number=%s""", (
            otp_code,
            to_phone_number,
        ))
        connection.commit()
        
        return Response(
            {
                'status_code': status.HTTP_200_OK,
                'result': 'OTP sent successfully'
            },
            status=status.HTTP_200_OK
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
                'result': 'OTP expired'
            },
            status=status.HTTP_200_OK
        )
