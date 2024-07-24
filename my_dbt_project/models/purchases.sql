{{ config(
    materialized='table'
) }}

SELECT
    purchase_id,
    symbol,
    amount,
    price,
    purchase_date
FROM alpaca_crypto_data.purchases
