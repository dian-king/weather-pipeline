import pandas as pd
from datetime import datetime, timezone
import logging

def transform(raw_records: list[dict]) -> pd.DataFrame:
    """Parse raw API responses into a clean, typed DataFrame."""
    rows = []
    for r in raw_records:
        try:
            row = {
                "city":          r["name"],
                "country":       r["sys"]["country"],
                "temperature":   r["main"]["temp"],
                "feels_like":    r["main"]["feels_like"],
                "humidity":      r["main"]["humidity"],
                "pressure":      r["main"]["pressure"],
                "wind_speed":    r["wind"]["speed"],
                "wind_deg":      r.get("wind", {}).get("deg"),
                "description":   r["weather"][0]["description"],
                "cloud_cover":   r["clouds"]["all"],
                "visibility":    r.get("visibility"),
                "rain_1h":       r.get("rain", {}).get("1h", 0.0),
                "recorded_at":   datetime.fromtimestamp(r["dt"], tz=timezone.utc),
                "fetched_at":    datetime.now(tz=timezone.utc),
            }
            rows.append(row)
        except KeyError as e:
            logging.warning(f"Missing field {e} in record for {r.get('name', 'unknown')}")

    df = pd.DataFrame(rows)

    if df.empty:
        return df

    # Validation: drop rows with nulls in critical columns
    df = df.dropna(subset=["city", "temperature", "humidity"])

    # Type enforcement
    df["temperature"] = df["temperature"].astype(float)
    df["humidity"]    = df["humidity"].astype(int)
    df["pressure"]    = df["pressure"].astype(int)

    logging.info(f"Transformed {len(df)} valid records")
    return df