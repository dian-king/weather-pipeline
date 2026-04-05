import schedule
import time
import logging
from extract import extract_all
from transform import transform
from load import load

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def run_pipeline():
    logging.info("=== Pipeline run starting ===")
    try:
        raw = extract_all()
        df  = transform(raw)
        load(df)
        logging.info("=== Pipeline run complete ===")
    except Exception as e:
        logging.error(f"Pipeline failed: {e}", exc_info=True)

if __name__ == "__main__":
    run_pipeline()                        # run once immediately on start
    schedule.every(1).hours.do(run_pipeline)

    logging.info("Scheduler started — running every hour. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)