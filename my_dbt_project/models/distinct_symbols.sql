{{ config(
    materialized='table'
) }}

SELECT DISTINCT
    symbol,
    NULL AS name,
    'crypto' AS type
FROM {{ ref('clean_crypto_data') }}
