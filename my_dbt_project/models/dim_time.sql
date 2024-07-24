-- models/dim_time.sql
{{ config(
    materialized='table'
) }}

WITH timestamps AS (
    SELECT DISTINCT CAST(timestamp AS TIMESTAMP) AS timestamp
    FROM {{ ref('clean_crypto_data') }}
)

SELECT
    ROW_NUMBER() OVER () AS time_id,
    timestamp,
    EXTRACT(YEAR FROM timestamp) AS year,
    EXTRACT(MONTH FROM timestamp) AS month,
    EXTRACT(DAY FROM timestamp) AS day,
    EXTRACT(HOUR FROM timestamp) AS hour,
    EXTRACT(MINUTE FROM timestamp) AS minute,
    EXTRACT(SECOND FROM timestamp) AS second
FROM timestamps
