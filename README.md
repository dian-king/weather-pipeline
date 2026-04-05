# Weather Data Pipeline

An end-to-end data engineering project that ingests real-time weather data
from the OpenWeatherMap API, transforms it, and stores it in PostgreSQL.
Runs automatically on an hourly schedule.

## Architecture

Extract (API) → Transform (pandas) → Load (PostgreSQL)

## Tech Stack

- Python 3.11
- PostgreSQL
- pandas
- SQLAlchemy
- psycopg2
- schedule
- python-dotenv

## Features

- Fetches live weather data for multiple cities every hour
- Cleans and validates data before loading
- Handles API failures gracefully with logging
- Stores historical readings for trend analysis

## Project Structure

weather_pipeline/
├── extract.py       # API ingestion layer
├── transform.py     # Data cleaning and validation
├── load.py          # PostgreSQL write layer
├── pipeline.py      # Orchestrator and scheduler
├── config.py        # Environment config loader
├── .env.example     # Template for environment variables
└── requirements.txt

## Setup

1. Clone the repository
   git clone https://github.com/your-username/weather-pipeline.git

2. Create and activate virtual environment
   python -m venv venv
   venv\Scripts\Activate.ps1

3. Install dependencies
   pip install -r requirements.txt

4. Copy .env.example to .env and fill in your credentials
   cp .env.example .env

5. Create the PostgreSQL database and table
   psql -U postgres -f schema.sql

6. Run the pipeline
   python pipeline.py

## Sample Output

| City    | Temp (°C) | Humidity | Description  |
|---------|-----------|----------|--------------|
| Kigali  | 22.71     | 68       | light rain   |
| Nairobi | 24.93     | 47       | broken clouds|
| Lagos   | 34.80     | 47       | broken clouds|
| London  | 12.46     | 51       | broken clouds|

## Author

King — Software Engineering Student, Kigali Rwanda