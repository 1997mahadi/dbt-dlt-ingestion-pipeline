import dlt
from datetime import datetime
from typing import Iterator
from .helpers import AlpacaCryptoApi
from .schemas import CryptoData, MetaData, PurchaseData

# Initialize the API client globally
api_client = AlpacaCryptoApi()

@dlt.resource(name="crypto_data", write_disposition="replace")
def crypto_data_generator(start_date: str, end_date: str, timeframe: str, symbols: str) -> Iterator[dict]:
    for symbol in symbols.split(','):
        data = api_client.fetch_crypto_data(symbol, start_date, end_date, timeframe)
        # Comment out or remove the print statements
        # print(f"Fetched {len(data)} records for {symbol}")  # Print number of records fetched
        for item in data:
            # print(f"Processing item: {item}")  # Print each item
            item['timestamp'] = item['timestamp'].strftime('%Y-%m-%dT%H:%M:%S%z')  # Ensure timestamp is a string
            yield item

@dlt.resource(name="metadata", write_disposition="replace")
def metadata_generator(start_date: str, end_date: str, symbols: str, timeframe: str) -> Iterator[dict]:
    metadata = MetaData(
        start_date=start_date,
        end_date=end_date,
        symbols=symbols.split(","),
        timeframe=timeframe
    )
    yield metadata.dict()

@dlt.resource(name="purchases", write_disposition="replace")
def purchases_generator(symbols: str, num_purchases: int = 100) -> Iterator[dict]:
    import random
    from datetime import datetime, timedelta
    symbols_list = symbols.split(",")
    for i in range(num_purchases):
        purchase = PurchaseData(
            purchase_id=i + 1,
            symbol=random.choice(symbols_list),
            amount=random.uniform(0.1, 5.0),
            price=random.uniform(30000, 60000),
            purchase_date=datetime.now() - timedelta(days=random.randint(0, 365))
        )
        yield purchase.dict()

@dlt.source(name="alpaca_crypto")
def alpaca_crypto_source(start_date: str, end_date: str, timeframe: str, symbols: str):
    yield crypto_data_generator(start_date, end_date, timeframe, symbols)
    yield metadata_generator(start_date, end_date, symbols, timeframe)
    yield purchases_generator(symbols)
