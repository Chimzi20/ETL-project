
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=os.getenv("POSTGRES_PORT", "5434"),
    database=os.getenv("POSTGRES_DB", "GFDR_Projects"),
    user=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS FEMA_data(
        disasterNumber INT,
        incidentType TEXT,
        projectSize TEXT
    )
""")

connection.commit()
