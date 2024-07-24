{{ config(
    materialized='table'
) }}

with symbol_mapping as (
    select
        symbol,
        symbol_id
    from {{ ref('dim_symbols') }}
)

select
    c.symbol,
    c.timestamp,
    c.open,
    c.high,
    c.low,
    c.close,
    c.volume,
    s.symbol_id
from {{ ref('clean_crypto_data') }} c
join symbol_mapping s on c.symbol = s.symbol
