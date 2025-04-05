import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

class GetConnection:
    @staticmethod
    def get_connection():
        # Only load .env if running locally
        if os.environ.get("VERCEL_ENV") is None:
            env_path = Path(__file__).resolve().parent.parent / '.env'
            load_dotenv(dotenv_path=env_path)
            print("Loaded .env from local")

        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")

        return psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            dbname=db_name
        )
