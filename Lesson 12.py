import logging
from datetime import date

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d"
)

today = date.today()

logging.info(f"Поточна дата: {today}")
