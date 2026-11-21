from pydantic import BaseModel
from typing import Dict, Optional, Union


class GoldRatesResponse(BaseModel):
    metal: str
    currency: str
    unit: str
    rates: Dict[str, float]
    source: str
    last_updated: Optional[Union[int, str]] = None


class SilverRatesResponse(BaseModel):
    metal: str
    currency: str
    unit: str
    price_per_gram: float
    price_per_kg: float
    source: str
    last_updated: Optional[Union[int, str]] = None


class AllMetalsResponse(BaseModel):
    gold: GoldRatesResponse
    silver: SilverRatesResponse
