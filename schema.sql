CREATE DATABASE weather_db;

\c weather_db

CREATE TABLE weather_readings (
    id           SERIAL PRIMARY KEY,
    city         VARCHAR(100) NOT NULL,
    country      VARCHAR(10),
    temperature  NUMERIC(5,2),
    feels_like   NUMERIC(5,2),
    humidity     INTEGER,
    pressure     INTEGER,
    wind_speed   NUMERIC(6,2),
    wind_deg     INTEGER,
    description  VARCHAR(200),
    cloud_cover  INTEGER,
    visibility   INTEGER,
    rain_1h      NUMERIC(6,2) DEFAULT 0,
    recorded_at  TIMESTAMPTZ,
    fetched_at   TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_city_time ON weather_readings (city, recorded_at DESC);