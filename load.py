import pandas as pd
from sqlalchemy import create_engine, text
from config import DB_CONFIG
import logging

def get_engine():
    cfg = DB_CONFIG
    url = (
        f"postgresql://{cfg['user']}:{cfg['password']}"
        f"@{cfg['host']}:{cfg['port']}/{cfg['dbname']}"
    )
    return create_engine(url)

def load(df: pd.DataFrame) -> None:
    """Append clean records to PostgreSQL."""
    if df.empty:
        logging.warning("Nothing to load — DataFrame is empty")
        return

    engine = get_engine()
    df.to_sql(
        name="weather_readings",
        con=engine,
        if_exists="append",   # never overwrites existing data
        index=False,
        method="multi",       # batch insert for efficiency
    )
    logging.info(f"Loaded {len(df)} rows into weather_readings")

def preview(n: int = 5) -> None:
    """Print the latest n rows from the table."""
    engine = get_engine()
    with engine.connect() as conn:
        result = conn.execute(text(
            f"SELECT city, temperature, humidity, description, fetched_at "
            f"FROM weather_readings ORDER BY fetched_at DESC LIMIT {n}"
        ))
        for row in result:
            print(row)