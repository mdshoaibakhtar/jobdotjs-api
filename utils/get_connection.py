
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class GetConnection:
    def get_connection():
        load_dotenv()
        return psycopg2.connect(
            host=os.getenv('HOST'),
            port=os.getenv('PORT'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            dbname=os.getenv('DBNAME'),
            sslmode='require'
        )