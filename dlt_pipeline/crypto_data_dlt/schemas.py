from pydantic import BaseModel
from datetime import datetime
from typing import List

class CryptoData(BaseModel):
    symbol: str
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

class MetaData(BaseModel):
    start_date: datetime
    end_date: datetime
    symbols: List[str]
    timeframe: str

class PurchaseData(BaseModel):
    purchase_id: int
    symbol: str
    amount: float
    price: float
    purchase_date: datetime
