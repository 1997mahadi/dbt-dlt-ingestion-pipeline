-- models/clean_crypto_data.sql

{{ config(
    materialized='table'
) }}

WITH ranked_data AS (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY symbol ORDER BY timestamp) AS rank
    FROM {{ ref('crypto_data') }}
)

SELECT
    symbol,
    timestamp,
    open,
    high,
    low,
    close,
    volume
FROM ranked_data
WHERE rank = 1
