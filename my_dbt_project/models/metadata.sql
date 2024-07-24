{{ config(
    materialized='table'
) }}

SELECT
    start_date,
    end_date,
    timeframe,
    _dlt_load_id,
    _dlt_id
FROM alpaca_crypto_data.metadata
