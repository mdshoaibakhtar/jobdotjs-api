import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

class GetConnection:
    @staticmethod
    def get_connection():
        # Load the environment variables from the .env file
        load_dotenv()
        # Retrieve the environment variables
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")

        # Return the database connection
        return psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            dbname=db_name
        )