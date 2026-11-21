import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Load the backend/.env file
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)

API_KEY = os.getenv("GOLD_API_KEY")
BASE_URL = "https://www.goldapi.io/api"

HEADERS = {
    "x-access-token": API_KEY or "",
    "Content-Type": "application/json"
}


def fetch_metal_data(symbol):
    """Fetch live metal prices from GoldAPI."""

    if not API_KEY:
        raise RuntimeError("GOLD_API_KEY is missing from the .env file")

    url = f"{BASE_URL}/{symbol}/INR"

    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("GoldAPI request timed out")

    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(
            f"GoldAPI returned HTTP error: {exc}"
        )

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            f"Unable to connect to GoldAPI: {exc}"
        )


def get_gold_rates():
    """Return live gold rates in INR per gram."""

    data = fetch_metal_data("XAU")

    rates = {
        "24K": data.get("price_gram_24k"),
        "22K": data.get("price_gram_22k"),
        "18K": data.get("price_gram_18k")
    }

    if any(value is None for value in rates.values()):
        raise RuntimeError("GoldAPI did not return all required gold purity prices")

    return {
        "metal": "Gold",
        "currency": "INR",
        "unit": "gram",
        "rates": rates,
        "source": "GoldAPI",
        "last_updated": data.get("timestamp")
    }


def get_silver_rates():
    """Return live silver rates in INR per gram and kilogram."""

    data = fetch_metal_data("XAG")

    price_per_gram = data.get("price_gram_24k")

    if price_per_gram is None:
        raise RuntimeError(
            "GoldAPI did not return the silver price per gram"
        )

    return {
        "metal": "Silver",
        "currency": "INR",
        "unit": "gram",
        "price_per_gram": price_per_gram,
        "price_per_kg": round(price_per_gram * 1000, 2),
        "source": "GoldAPI",
        "last_updated": data.get("timestamp")
    }
