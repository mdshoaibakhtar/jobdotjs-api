from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2.extras import RealDictCursor

class GetConnection:
    @staticmethod
    def get_connection():
        # Set path to the .env file explicitly
        print('Load connection details')
        env_path = Path(__file__).resolve().parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")

        print("db_host:", db_host)
        print("db_password:", db_password)

        return psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            dbname=db_name
        )
