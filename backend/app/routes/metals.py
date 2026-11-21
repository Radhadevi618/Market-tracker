from fastapi import APIRouter

from app.models.metals import (
    GoldRatesResponse,
    SilverRatesResponse,
    AllMetalsResponse
)

from app.services.metals_service import (
    get_gold_rates,
    get_silver_rates
)

router = APIRouter(
    prefix="/api/metals",
    tags=["Metals"]
)


@router.get(
    "/gold",
    response_model=GoldRatesResponse,
    summary="Gold Rates"
)
def gold_rates():
    """Get gold prices in India."""
    return get_gold_rates()


@router.get(
    "/silver",
    response_model=SilverRatesResponse,
    summary="Silver Rates"
)
def silver_rates():
    """Get silver prices in India."""
    return get_silver_rates()


@router.get(
    "",
    response_model=AllMetalsResponse,
    summary="All Metal Rates"
)
def all_metal_rates():
    """Get both gold and silver prices."""
    return {
        "gold": get_gold_rates(),
        "silver": get_silver_rates()
    }
