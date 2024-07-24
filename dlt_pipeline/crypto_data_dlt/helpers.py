from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame

class AlpacaCryptoApi:
    def __init__(self):
        self.client = CryptoHistoricalDataClient()

    def fetch_crypto_data(self, symbol: str, start: str, end: str, timeframe: str):
        # Map the timeframe string to the appropriate TimeFrame unit
        if timeframe == "Day":
            timeframe_unit = TimeFrame.Day
        elif timeframe == "Hour":
            timeframe_unit = TimeFrame.Hour
        elif timeframe == "Minute":
            timeframe_unit = TimeFrame.Minute
        else:
            raise ValueError(f"Invalid timeframe: {timeframe}")

        request_params = CryptoBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=timeframe_unit,
            start=start,
            end=end
        )
        data = self.client.get_crypto_bars(request_params).df.reset_index().to_dict('records')
        return data
