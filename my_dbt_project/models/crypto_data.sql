{{ config(
    materialized='table'
) }}

SELECT
    symbol,
    timestamp,
    open,
    high,
    low,
    close,
    volume
FROM alpaca_crypto_data.crypto_data
