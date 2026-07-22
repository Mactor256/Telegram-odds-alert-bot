import requests

from config import (
    ODDS_API_KEY,
    MIN_ODDS
)


def fetch_odds():

    url = "https://the-odds-api.com"

    headers = {
        "X-API-Key":
        ODDS_API_KEY
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    data = response.json()

    results = []

    for match in data:

        if match["odds"] >= MIN_ODDS:

            results.append(
                {
                    "event":
                    match["event"],

                    "market":
                    match["market"],

                    "odds":
                    match["odds"]
                }
            )

    return results
