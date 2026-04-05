import os
from dotenv import load_dotenv

load_dotenv()

API_KEY  = os.getenv("OWM_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
CITIES   = os.getenv("CITIES", "Kigali").split(",")

DB_CONFIG = {
    "host":     os.getenv("DB_HOST", "localhost"),
    "port":     os.getenv("DB_PORT", "5432"),
    "dbname":   os.getenv("DB_NAME", "weather_db"),
    "user":     os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", ""),
}