import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

class Database:
    _instance = None  # No multi connections

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            load_dotenv()
            cls._instance.connection = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT')
            )
            cls._instance.connection.autocommit = True
            cls._instance.table = "contacts"
            cls._instance.ensure_table()
        return cls._instance

    def ensure_table(self):
        with self.connection.cursor() as cursor:
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(15) NOT NULL
            );
            """)

    def execute(self, query, params=None):
        with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params or ())
            try:
                return cursor.fetchall()
            except psycopg2.ProgrammingError:
                return []