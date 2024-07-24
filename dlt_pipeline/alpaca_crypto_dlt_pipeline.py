import dlt
from dlt.common.typing import TAnyDateTime
from crypto_data_dlt import alpaca_crypto_source

def load_crypto_data(start_date: TAnyDateTime, end_date: TAnyDateTime, timeframe: str, symbols: str) -> None:
    """Execute a pipeline that will load Alpaca crypto data within the given date range."""
    pipeline = dlt.pipeline(
        pipeline_name="alpaca_crypto",
        destination='duckdb',  # Using DuckDB as the destination
        dataset_name="alpaca_crypto_data",
        export_schema_path="schemas/export"
    )

    # Run the pipeline with Alpaca crypto source for the specified date range
    load_info = pipeline.run(
        alpaca_crypto_source(start_date=start_date, end_date=end_date, timeframe=timeframe, symbols=symbols)
    )
    print(load_info)  # This will print only the metadata about the load operation

if __name__ == "__main__":
    # Example usage:
    start_date = "2022-01-01"
    end_date = "2024-07-10"
    timeframe = "Day"  # Corrected timeframe
    symbols = "BTC/USD"

    load_crypto_data(start_date=start_date, end_date=end_date, timeframe=timeframe, symbols=symbols)
