
import boto3
import psycopg2
from psycopg2.extras import RealDictCursor
# from dotenv import load_dotenv
import os

class GetConnection:
    def get_connection():
        # load_dotenv()
        return psycopg2.connect(
            host='ep-divine-block-a4qsr7yt-pooler.us-east-1.aws.neon.tech',
            port='5432',
            user='default',
            password='LTqX4YxZ5eQt',
            dbname='verceldb',
            sslmode='require'
        )