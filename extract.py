import requests
import logging
from config import API_KEY, BASE_URL, CITIES

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def fetch_weather(city: str) -> dict | None:
    """Fetch current weather for a city. Returns raw JSON or None on failure."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        logging.info(f"Fetched data for {city}")
        return response.json()
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error for {city}: {e}")
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection failed for {city}")
    return None

def extract_all() -> list[dict]:
    """Run extraction for all configured cities."""
    results = []
    for city in CITIES:
        data = fetch_weather(city.strip())
        if data:
            results.append(data)
    return results