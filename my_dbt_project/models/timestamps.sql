{{ config(
    materialized='table'
) }}

WITH timestamps AS (
    SELECT DISTINCT CAST(timestamp AS timestamp) AS timestamp
    FROM {{ ref('clean_crypto_data') }}
)

SELECT
    timestamp,
    extract(year FROM timestamp) AS year,
    extract(month FROM timestamp) AS month,
    extract(day FROM timestamp) AS day,
    extract(hour FROM timestamp) AS hour,
    extract(minute FROM timestamp) AS minute,
    extract(second FROM timestamp) AS second
FROM timestamps
