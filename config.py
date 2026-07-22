import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

ODDS_API_KEY = os.getenv(
    "ODDS_API_KEY"
)

MIN_ODDS = float(
    os.getenv(
        "MIN_ODDS",
        2.00
    )
)
