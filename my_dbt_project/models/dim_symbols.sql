-- models/dim_symbols.sql
{{ config(
    materialized='table'
) }}

SELECT
    ROW_NUMBER() OVER () AS symbol_id,
    symbol,
    NULL AS name,
    'crypto' AS type
FROM {{ ref('distinct_symbols') }}
